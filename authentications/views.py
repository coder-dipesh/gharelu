from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from authentications.models import UserSignUp
from .forms import CreateUserForm
from passlib.hash import pbkdf2_sha256

# Methodes goes here
def login(request):
    context={}
    return render(request, 'authentications/login.html',context)


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + 'your account created successfully.')

            return redirect('login')

    context = {'form':CreateUserForm}
    return render(request, 'authentications/signup.html',context)
