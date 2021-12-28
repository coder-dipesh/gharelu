from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from .auth import unauthenticated_user



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
            messages.error(request, "Username or Password is incorrect.")
            return redirect('signin')
    context={}
    return render(request, 'authentications/login.html',context)


def signup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'User registered successfully!' )
            return redirect('/auth/signin')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register user' )
            return render(request, 'authentications/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'authentications/signup.html', context)



def proSignup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            user=userdata.save()
            user.is_staff = True  # This is for professional user registration
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Professional registered successfully.' )
            return redirect('/auth/signin')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register as Professionals!' )
            return render(request, 'authentications/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'authentications/signup.html', context)



def signout(request):
    logout(request)
    return redirect('/auth/signin')