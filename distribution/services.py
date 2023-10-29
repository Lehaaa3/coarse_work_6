from django.core.mail import send_mail
from django.conf import settings
from distribution.models import Message, MailingSettings, Log


def send_email(title, text, emails):
    send_mail(
        subject=title,
        message=text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[emails],
        fail_silently=False,
    )
