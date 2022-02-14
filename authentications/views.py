import random
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from .forms import CreateUserForm
from django.contrib.auth.forms import PasswordChangeForm
from .auth import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .models import Profile, UserOTP
from django.core.mail import send_mail
from django.conf import settings
import uuid

# Methodes goes here

# @unauthenticated_user
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


# @unauthenticated_user
def proSignup(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username = get_usr)

            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.is_staff = True
                usr.save()
                Profile.objects.create(user=usr, username=usr.username, email= usr.email)
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

    context = {'form':CreateUserForm}
    return render(request, 'account/signup.html', context)  


def signout(request):
    logout(request)
    return redirect('/')


# @unauthenticated_user
def userSignup(request):

    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username = get_usr)

            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                Profile.objects.create(user=usr, username=usr.username, email= usr.email)

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

    context = {'form':CreateUserForm}
    return render(request, 'account/signup.html', context)  


def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://localhost:8000/auth/reset-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def entermailResetpassword(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.add_message(request, messages.ERROR, f'No user found with {username} username.')
                return redirect('/auth/reset-password-enterusername')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())

            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()

            send_forget_password_mail(user_obj.email , token)
            messages.add_message(request,messages.SUCCESS, 'An email is sent to user with password changing link.')
            return redirect('/auth/reset-password-enterusername')

    return render(request, 'account/reset-password-enterusername.html')

def resetPassword(request,token):
    profile_obj = Profile.objects.filter(forget_password_token = token).first()
    context = {'user_id' : profile_obj.user.id}
        
    if request.method == 'POST':
        new_password = request.POST.get('password-1')
        confirm_new_password = request.POST.get('password-2')
        user_id = request.POST.get('user_id')

        
        if user_id is  None:
            messages.add_message(request, messages.ERROR ,'No user found with that username.')
            return redirect(f'/reset-password/{token}/')
            
        if  new_password != confirm_new_password:
            messages.add_message(request, messages.ERROR ,'Password must be equal.')
            return redirect(f'/auth/reset-password/{token}/')
            
        print(user_id)
        user_obj = User.objects.get(id = user_id)
        print(user_obj)

        user_obj.set_password(new_password)
        user_obj.save()

        return render(request, 'account/reset-password-done.html')


    return render(request, 'account/reset-password.html', context)

def resetpasswordDone(request):
    messages.add_message(request, messages.SUCCESS ,'Password reset')

    return render(request, 'account/reset-password-done.html')

# @login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/auth/change-password')
        else:
            messages.add_message(request, messages.ERROR, "Please check the fields")
            return render(request, 'account/change-password.html' ,{'user_password_change_form':form})
    context = {
        'user_password_change_form': PasswordChangeForm(request.user),

    }
    return render(request, 'account/change-password.html', context)




