from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_token
from email import message
from LoginAPI.models import User


def send_email(user, request):
    
    currnet_site = get_current_site(request)
    email_sub = 'Verify Your Email'
    email_body = render_to_string('authentication/verify.html', {
        'user':user,
        'domain':currnet_site,
        'uid':urlsafe_base64_encode(force_bytes(user.id)),
        'token':generate_token.make_token(user)
    })
    
    message = EmailMessage(subject=email_sub, body=email_body,from_email=settings.EMAIL_FROM_USER,
                 to=[user.email])
    
    message.send()


def verify_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        
        user = User.objects.get(id=uid)
        
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        user.isVerified = True
        user.save()
    
        messages.add_message(request, messages.SUCCESS, 'Email Verified')
        return redirect('http://127.0.0.1:8000/user/')
    
    return render(request, 'authentication/verificationFailed.html')