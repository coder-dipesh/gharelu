from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


# Methodes goes here
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect('login')
    context={}
    return render(request, 'authentications/login.html',context)


def signup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'User registered successfully!' )
            return redirect('/auth/login')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register user' )
            return render(request, 'authentications/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'authentications/signup.html', context)




def home(request):
    return render(request, 'authentications/home.html')