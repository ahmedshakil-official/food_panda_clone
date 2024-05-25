from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_notification_email(subject, template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(template, context)
    to_email = context["user"].email
    mail = EmailMessage(subject, message, from_email, to=[to_email])
    mail.send()
