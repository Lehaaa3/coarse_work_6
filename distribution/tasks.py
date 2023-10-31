from distribution.services import send_mailling
from distribution.models import MailingSettings


def daily_tasks():
    mailings = MailingSettings.objects.filter(periodicity="Раз в день", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def weekly_tasks():
    mailings = MailingSettings.objects.filter(periodicity="Раз в неделю", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def monthly_tasks():
    mailings = MailingSettings.objects.filter(periodicity="Раз в месяц", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)
