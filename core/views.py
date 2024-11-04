from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from .models import PasswordEntry
from .utils import generate_password

class HomeView(TemplateView):
    template_name = "home.html"
    

class SolutionsView(TemplateView):
    template_name = "solutions.html"
    


def password_list(request):
    passwords = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'password_list.html', {'passwords': passwords})

def add_password(request):
    if request.method == 'POST':
        website = request.POST['website']
        username = request.POST['username']
        raw_password = request.POST['password']
        password_entry = PasswordEntry(website=website, username=username)
        password_entry.set_password(raw_password)
        password_entry.save()
        return redirect('password_list')
    return render(request, 'add_password.html', {'generated_password': generate_password()})






























def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact.save()

            # Prepare email details
            subject = "New Contact Form Submission"
            message = f"""
            You've received a new message!

            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Message: {form.cleaned_data['message']}
            """
            from_email = 'no-reply@yourdomain.com'
            recipient_list = ['zahidhasan9297@gmail.com']  # Your email to receive the message

            try:
                send_mail(subject, message, from_email, recipient_list)
                return redirect('success')
            except Exception as e:
                # Log or handle any email sending errors
                print(f"Error sending email: {e}")
                return render(request, 'contact.html', {'form': form, 'error': 'Error sending email'})

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
