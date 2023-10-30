from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone
from django.utils import timezone

from distribution.models import Message, MailingSettings, Log, Client


def daily_tasks():
    mailings = MailingSettings.objects.filter(status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def send_mailling(mailing: MailingSettings):
    now = timezone.localtime(timezone.now())
    for mail_settings in mailing.objects.filter(status="Запущена"):
        if mail_settings.start_time <= now <= mail_settings.end_time:
            for message in mail_settings.messages.filter(status="К отправке"):
                emails_for_send = []
                for client in mail_settings.clients.all():
                    emails_for_send.append(client.email)
                send_mail(
                    subject=message.title,
                    message=message.text,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[*emails_for_send],
                    fail_silently=False
                )
                message.status = Message.SHIPPED
                message.save()

