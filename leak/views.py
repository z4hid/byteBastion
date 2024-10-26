import requests
from django.shortcuts import render

from django.conf import settings
from .forms import LeakForm
from .models import LeakResult



def check_leak(request):
    result = None
    if request.method == 'POST':
        form = LeakForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            
            # Make API request
            api_url = f'https://leakcheck.net/api/public?check={username_or_email}'

            
            try:
                response = requests.get(api_url, params=api_url)
                data = response.json()
                print(data.get('success'))
                
                if data.get('success'):
                    # Save to database
                    result = LeakResult.objects.create(
                        username_or_email=username_or_email,
                        found_count=data.get('found', 0),
                        fields=data.get('fields', []),
                        sources=data.get('sources', [])
                    )
                    
                    print(result)
                    
                else:
                    result="secured"
                
            except Exception as e:
                print(f"Error: {e}")
    else:
        form = LeakForm()
    
    return render(request, 'check.html', {
        'form': form,
        'result': result
    })
