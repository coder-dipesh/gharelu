from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import professional_only
from authentications.forms import ProfileForm

# Create your views here.

@login_required
@professional_only
def professionalDashboard(request):
    return render(request, 'professionals/professionalDashboard.html')



@login_required
@professional_only
def professionalProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    if request.method == 'POST':
        userdata = ProfileForm(request.POST, request.FILES, instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/professionals/professionalprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileForm':userdata}
            return render(request, 'professionals/professionalProfile.html',context)

    context = {'profileForm':ProfileForm(instance=profile)}
    return render(request, 'professionals/professionalProfile.html', context)

import os

@login_required
@professional_only
def professionalUpdateProfile(request):
    profile= request.user.profile # Getting currently logged in user data



    if request.method == 'POST':
        # Delete image from uploads static after changing new image
        os.remove(profile.profile_pic.path)

        userdata = ProfileForm(request.POST,request.FILES,instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/professionals/professionalupdateprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileUpdateForm':userdata}
            return render(request, 'professionals/professionalUpdateProfile.html',context)

    context = {'profileUpdateForm':ProfileForm(instance=profile)}
    return render(request, 'professionals/professionalUpdateProfile.html', context)

    