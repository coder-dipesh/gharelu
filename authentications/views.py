from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, MyCustomSignupForm
from .auth import unauthenticated_user
from allauth.account.views import SignupView


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
def userSignup(request):

    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            userdata.save()
            
            messages.add_message(request, messages.SUCCESS, 'User registered successfully!' )
            return redirect('/auth/signin')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register user' )
            return render(request, 'account/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'account/signup.html', context)


@unauthenticated_user
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
            return render(request, 'account/signup.html',context)


    context ={'form' : CreateUserForm}
    return render(request, 'account/signup.html', context)



def signout(request):
    logout(request)
    return redirect('/auth/signin')

class AllauthSignUpView(SignupView):
    template_name = 'account/signup.html'
    form_class = MyCustomSignupForm
    # success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        print("test")
        context = super(AllauthSignUpView, self).get_context_data(**kwargs)
        signUpForm = MyCustomSignupForm(self.request.POST or None)
        context['form'] = signUpForm
        return context

    