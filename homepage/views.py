from django.shortcuts import render
from professionals.models import Service
from .filters import ServiceFilter


def homepage(request):
    return render(request,'homepage/homepage.html')

def about(request):
    return render(request,'homepage/about.html')

def service(request):
    services = Service.objects.all().order_by('-id')
    service_filter = ServiceFilter(request.GET, queryset=services)

    services_final = service_filter.qs 

    context = {'services':services_final , 'service_filter':service_filter}
    return render(request,'homepage/service.html',context)


