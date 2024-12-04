# service/urls.py

from django.urls import path
from .views import ServiceListView, ServiceDetailView

app_name = 'service'  # This sets the namespace for the app

urlpatterns = [
    path('list/', ServiceListView.as_view(), name='service-list'),
    path('details/<int:pk>/', ServiceDetailView.as_view(), name='service-details'),
]
