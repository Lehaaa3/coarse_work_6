from django.forms import ModelForm

from distribution.models import Message, MailingSettings


class MailingSettingsForm(ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('start_time', 'end_time', 'periodicity', 'status', 'clients',)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text', 'status',)
