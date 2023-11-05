from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone
from django.utils import timezone

from distribution.models import Message, MailingSettings, Log, Client


def send_mailling(mailing):
    now = timezone.localtime(timezone.now())
    if mailing.start_time <= now <= mailing.end_time:
        for message in mailing.messages.all():
            for client in mailing.clients.all():
                try:
                    result = send_mail(
                        subject=message.title,
                        message=message.text,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )
                    log = Log.objects.create(
                        time=mailing.start_time,
                        status=result,
                        server_response='OK',
                        mailing_list=mailing,
                        client=client
                    )
                    log.save()
                    return log
                except SMTPException as error:
                    log = Log.objects.create(
                        time=mailing.start_time,
                        status=False,
                        server_response=error,
                        mailing_list=mailing,
                        client=client
                    )
                    log.save()
                return log
    else:
        mailing.status = MailingSettings.COMPLETED
        mailing.save()
