from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def detect_user(user):
    if user.role == 1:
        return "vendor-dashboard"
    elif user.role == 2:
        return "customer-dashboard"
    elif user.role is None and user.is_superuser:
        return "/admin"


def send_verification_email(request, user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    email_subject = "Please Verify And Activate Your Account"
    message = render_to_string(
        "accounts/email/verification.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        },
    )
    to_email = user.email
    mail = EmailMessage(email_subject, message, from_email, to=[to_email])
    mail.send()


def send_password_reset_email(request, user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    email_subject = "If you want to Reset Your Password click link bellow."
    message = render_to_string(
        "accounts/email/password_reset.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        },
    )
    to_email = user.email
    mail = EmailMessage(email_subject, message, from_email, to=[to_email])
    mail.send()
