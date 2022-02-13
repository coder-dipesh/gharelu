from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from customers.forms import FeedbackForm
from customers.models import Feedback
from authentications.auth import customer_only
from authentications.forms import ProfileForm
from django.contrib import messages
from homepage.models import Order
from professionals.models import Service
from homepage.filters import ServiceFilter

# Create your views here.

@login_required
@customer_only
def customerDashboard(request):
    services = Service.objects.all().order_by('-id')
    service_filter = ServiceFilter(request.GET, queryset=services)

    services_final = service_filter.qs 

    context = {'services':services_final , 'service_filter':service_filter}
    return render(request, 'customers/customerDashboard.html',context)


@login_required
@customer_only
def customerProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    if request.method == 'POST':
        userdata = ProfileForm(request.POST, request.FILES, instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/customers/customerprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileForm':userdata}
            return render(request, '/customers/customerProfile.html',context)

    context = {'profileForm':ProfileForm(instance=profile)}
    return render(request, 'customers/customerProfile.html', context)


@login_required
@customer_only
def customerUpdateProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    print(profile)
    if request.method == 'POST':
        print('hello')


        userdata = ProfileForm(request.POST,request.FILES,instance=profile) 
        print(userdata)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/customers/customerupdateprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileUpdateForm':userdata}
            return render(request, 'customers/customerUpdateProfile.html',context)

    context = {'profileUpdateForm':ProfileForm(instance=profile)}
    return render(request, 'customers/customerUpdateProfile.html', context)

@login_required
@customer_only
def myBookings(request):
    user = request.user
    servicePending = Order.objects.filter(user=user, status="Pending").order_by('-id')
    serviceApproved = Order.objects.filter(user=user, status="Approved").order_by('-id')
    serviceDeclined = Order.objects.filter(user=user, status="Declined").order_by('-id')
    context = {
        'servicePending': servicePending,
        'serviceApproved': serviceApproved,
        'serviceDeclined': serviceDeclined,
        'activate_mybookings': 'active'
    }
    return render(request, 'customers/myBookings.html',context)

@login_required
@customer_only
def feedbackForm(request, service_id):
    user_id = request.user
    service_id = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data=Feedback()
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.service_feedback = form.cleaned_data['service_feedback']
            data.user = user_id
            data.service = service_id
            data.save()

            messages.add_message(request, messages.SUCCESS, 'Thank You! Your Feedback submitted successfully!')
            return redirect('/customers/feedback_form/'+str(service_id.id))
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            return redirect('/customers/feedback_form/'+str(service_id.id))

    context={
        'form_feedback':FeedbackForm()

    }


    return render(request, 'customers/feedbackForm.html', context)