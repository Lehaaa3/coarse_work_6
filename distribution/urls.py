from django.urls import path

from distribution.apps import DistributionConfig
from distribution.views import MailingSettingsDetailView, MailingSettingsListView, MailingSettingsCreateView, \
    MailingSettingsDeleteView, MailingSettingsUpdateView, ClientListView, ClientCreateView, ClientUpdateView, \
    LogListView

app_name = DistributionConfig.name

urlpatterns = [
    path('log', LogListView.as_view(), name='log_list'),
    path('clients/edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('clients/create', ClientCreateView.as_view(), name='create_client'),
    path('clients', ClientListView.as_view(), name='clients_list'),
    path('distribution/<int:pk>/', MailingSettingsDetailView.as_view(), name='distribution_detail'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='distribution_delete'),
    path('', MailingSettingsListView.as_view(), name='distribution_list'),
    path('create', MailingSettingsCreateView.as_view(), name='create_distribution'),
    path('edit/<int:pk>/', MailingSettingsUpdateView.as_view(), name='distribution_edit'),
]
