from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.core.validators import validate_email

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
    
            if not name or not email or not subject or not message:
                form.add_error(None, 'يرجى ملء جميع الحقول.')
                return render(request, 'contact_form.html', {'form': form})

            try:
                validate_email(email)
            except ValidationError:
                form.add_error('email', 'البريد الإلكتروني غير صالح')
                return render(request, 'contact_form.html', {'form': form})

            try:
                send_mail(
                    f'رسالة من {name} - {subject}',
                    message,
                    email,
                    [settings.CONTACT_EMAIL], 
                    fail_silently=False,
                )
            except Exception as e:
                form.add_error(None, 'حدث خطأ أثناء إرسال الرسالة، يرجى المحاولة لاحقًا.')
                return render(request, 'contact_form.html', {'form': form})
            
            return render(request, 'thank_you.html')
        else:
            return render(request, 'contact_form.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
