from distribution.services import send_mailling
from distribution.models import MailingSettings


def daily_tasks():
    mailings = MailingSettings.objects.filter(periodicity="DAILY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def weekly_tasks():
    mailings = MailingSettings.objects.filter(periodicity="WEEKLY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def monthly_tasks():
    mailings = MailingSettings.objects.filter(periodicity="MONTHLY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)