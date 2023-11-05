from django.forms import ModelForm

from distribution.models import Message, MailingSettings, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingSettingsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('start_time', 'end_time', 'periodicity', 'status', 'clients',)


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text',)


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('FIO', 'email', 'comment',)
