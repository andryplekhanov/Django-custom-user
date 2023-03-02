from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _


def send_email_for_verify(request, user):
    """ sends email for verification """
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'app_users/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        _('Please, confirm registration'),
        message,
        to=[user.email],
    )
    email.send()


def authenticate_user(form):
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password1')
    user = authenticate(email=email, password=password)
    return user
