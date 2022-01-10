<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from homepage.models import Feedback
from .forms import FeedbackForm
from django.contrib import messages


from authentications.auth import admin_only

def home(request):
    return render(request,'homepage/home.html')


def error404(request, exception):
    return render(request,'error404.html')

=======
from django.shortcuts import redirect, render
from authentications.auth import customer_only
from homepage.forms import OrderForm
from homepage.models import Order
from professionals.models import Service
from .filters import ServiceFilter
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
>>>>>>> 9e3cca5b061039e2e9940c673a71d882929e213a

def homepage(request):
    return render(request,'homepage/homepage.html')

def about(request):
    return render(request,'homepage/about.html')

<<<<<<< HEAD
=======

>>>>>>> 9e3cca5b061039e2e9940c673a71d882929e213a
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


@admin_only
def get_feedback(request):
    feedback = Feedback.objects.all().order_by('id')
    context = {
        'feedback': feedback,
        'activate_contact': 'active'
    }
    return render(request, 'admins/get_feedback.html', context)
