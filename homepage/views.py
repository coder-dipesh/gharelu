from django.shortcuts import redirect, render
from admins.models import Feedback
from customers.forms import FeedbackForm

from professionals.models import Service
from .filters import ServiceFilter
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

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

# Send feedback for purchased item
@login_required
def give_feedback(request):
    form = FeedbackForm
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Feedback sucessfully Sent")
            return redirect('/homepage/about')
        else:
            messages.add_message(request, messages.ERROR, "Unable to Send Feedback")
            return render(request, 'homepage/giveFeedback.html', {'form_feedback': form})
    context = {
        'form_feedback': FeedbackForm,
        'activate_contact': 'active'
    }
    return render(request, 'homepage/giveFeedback.html', context)



def Support(request):
    return render(request,'homepage/service.html')