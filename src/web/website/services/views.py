from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Service, ServiceCategory


# Service listing view
class ServiceListView(ListView):
    model = Service
    template_name = 'website/service.html'  # Path to your service listing template
    context_object_name = 'services'  # How you access the services in the template

    def get_queryset(self):
        # Only display active services
        return Service.objects.filter(is_active=True)


# Service detail view
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'website/service-details.html'  # Path to your service detail template
    context_object_name = 'service'  # How you access the service in the template
