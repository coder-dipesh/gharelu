from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from django.contrib import messages
from authentications.forms import ProfileForm

@login_required
@admin_only
def adminDashboard(request):
    return render(request, 'admins/adminDashboard.html' )



@login_required
@admin_only
def adminProfile(request):
    profile= request.user.profile # Getting currently logged in user data
    if request.method == 'POST':
        userdata = ProfileForm(request.POST, request.FILES, instance=profile) 
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Profile data updated successfully!')
            return redirect('/admins/adminprofile')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong!")
            context={'profileForm':userdata}
            return render(request, 'admins/adminProfile.html',context)

    context = {'profileForm':ProfileForm(instance=profile)}
    return render(request, 'admins/adminProfile.html', context)
