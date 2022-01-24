from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authentications.auth import customer_only
from authentications.forms import ProfileForm
from django.contrib import messages


# Create your views here.

@login_required
@customer_only
def customerDashboard(request):
    return render(request, 'customers/customerDashboard.html')


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


import os

@login_required
@customer_only
def customerUpdateProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    print(profile)


    if request.method == 'POST':
        print('hello')
        # Delete image from uploads static after changing new image
        # os.remove(profile.profile_pic.path)

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
