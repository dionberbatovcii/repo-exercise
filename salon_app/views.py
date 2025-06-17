from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'salon_app/landing_page.html', {'services': services})
