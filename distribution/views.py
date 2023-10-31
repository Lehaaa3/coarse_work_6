from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.forms import inlineformset_factory

from distribution.forms import MessageForm, MailingSettingsForm, ClientForm
from distribution.models import Client, MailingSettings, Message, Log


class GetContextDataMixin:

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingSettings, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            formset = MessageFormset(self.request.POST, instance=self.object)
        else:
            formset = MessageFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView, ClientForm):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('distribution:clients_list')


class ClientUpdateView(CreateView, UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('distribution:clients_list')


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsListView(ListView):
    model = MailingSettings

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['active'] = context_data['object_list'].filter(status=MailingSettings.STARTED).count()

        mailing_list = context_data['object_list'].prefetch_related('clients')
        clients = set()
        [[clients.add(client.email) for client in mailing.clients.all()] for mailing in mailing_list]
        context_data['clients_count'] = len(clients)
        return context_data


class MailingSettingsCreateView(GetContextDataMixin, Client, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('distribution:distribution_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings

    def get_success_url(self):
        return reverse('distribution:distribution_list')


class MailingSettingsUpdateView(GetContextDataMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('distribution:distribution_detail', args=[self.object.pk])


class LogListView(ListView):
    model = Log
