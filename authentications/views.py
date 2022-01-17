from multiprocessing import context
import random
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from .auth import unauthenticated_user
from .models import Profile, UserOTP
from django.core.mail import send_mail
from django.conf import settings

# Methodes goes here
@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if user.is_superuser and user.is_staff and user.is_active:
                return redirect('/admins')
            elif not user.is_superuser and user.is_staff and user.is_active:
                return redirect('/professionals')
            elif not user.is_superuser and not user.is_staff and user.is_active:
                return redirect('/customers')
        else:
            print("test")
            messages.error(request, "Username or Password is incorrect.")
            return render(request, 'account/login.html',{})
    context={}
    return render(request, 'account/login.html',context)



@unauthenticated_user
def proSignup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            user=userdata.save()
            user.is_staff = True  # This is for professional user registration
            user.save()
            Profile.objects.create(user=user, username=user.username, email= user.email) 

            messages.add_message(request, messages.SUCCESS, 'Professional registered successfully.' )
            return redirect('/auth/signin')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register as Professionals!' )
            return render(request, 'account/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'account/signup.html', context)



def signout(request):
    logout(request)
    return redirect('/')




@unauthenticated_user
def userSignup(request):

    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username = get_usr)

            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()

                messages.add_message(request, messages.SUCCESS, f'{usr.username} verified and registered successfully!')
                return redirect('signin')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid OTP! Please check again. ')
                
                return render(request, 'account/signup.html', {'otp':True, 'usr':usr})

        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            userdata.save()
            username = userdata.cleaned_data.get('username')

            usr = User.objects.get(username = username)
            usr.is_active= False
            usr.save()

            usr_otp = random.randint(100000, 999999)
            db_otp = usr_otp
            UserOTP.objects.create(user=usr, otp=db_otp)

            mail_message = f"Hello {usr.username}, \nYour OTP is {usr_otp}.\nThank You!\nTeam Gharelu. "

            send_mail(
                "Welcome to Gharelu -  Verify Your Email",
                mail_message,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently= False
            )
            return render(request, 'account/signup.html', {'otp':True, 'usr':usr})

    else:
        context = {'form':CreateUserForm}
    return render(request, 'account/signup.html', context)  
