from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
import os
import requests
from PIL import Image

from .utils import ImageConverter
from .models import MalwareDetection

from django.utils import timezone
import time

def upload_page(request):
    if request.method != 'POST':
        return render(request, 'malware-detect.html')

    file = request.FILES.get('file')

    if file is None:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    # Save the original uploaded file permanently
    original_file_name = default_storage.save(f"original/{file.name}", file)
    original_file_path = os.path.join(settings.MEDIA_ROOT, original_file_name)

    # Convert the file to RGB image and save as PNG
    converter = ImageConverter()
    rgb_image = converter.create_rgb_image(original_file_path)
    png_file_name = f"{os.path.splitext(file.name)[0]}.png"

    # Ensure the 'converted' directory exists
    converted_dir = os.path.join(settings.MEDIA_ROOT, 'converted')
    if not os.path.exists(converted_dir):
        os.makedirs(converted_dir)

    png_file_path = os.path.join(converted_dir, png_file_name)
    rgb_image.save(png_file_path, format='PNG')

    # Calculate file size
    file_size_kb = os.path.getsize(png_file_path) / 1024  # Size in KB
    file_size_str = f"{file_size_kb:.2f} KB"

    # Mock scan time calculation
    start_time = time.time()  # Start time before sending the request
    fastapi_url = 'https://z4hid-hf-cloud-fastapi.hf.space/predict'
    
    try:
        with open(png_file_path, 'rb') as f:
            files = {'file': (os.path.basename(png_file_path), f, 'image/png')}
            response = requests.post(fastapi_url, files=files)
            response.raise_for_status()
            result = response.json()

            # Extract the prediction and prepare other details
            prediction = result.get('prediction', 'Unknown')
            scan_time_seconds = time.time() - start_time  # Calculate scan time
            scan_time_str = f"{scan_time_seconds:.2f} seconds"

            # Create a result dictionary
            result_data = {
                "file_name": os.path.basename(png_file_path),
                "file_type": "image/png",
                "file_size": file_size_str,
                "scan_time": scan_time_str,
                "prediction": prediction
            }

            # Log the request and response details
            MalwareDetection.objects.create(
                image_name=os.path.basename(png_file_path),
                response_status=response.status_code,
                response_data=prediction,
                error_message=None
            )

        return render(request, 'malware-detect.html', {'result': result_data})

    except requests.RequestException as e:
        error_message = f'Error communicating with the API: {str(e)}'

        MalwareDetection.objects.create(
            image_name=os.path.basename(png_file_path),
            response_status=500,
            response_data=None,
            error_message=error_message
        )

        return render(request, 'malware-detect.html', {'error': error_message})
