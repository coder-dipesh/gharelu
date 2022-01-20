from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm

from authentications.models import Profile

class CreateUserForm(UserCreationForm):

    # Overriding usercreatiion form to design signup page
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-input',
            'placeholder':'Username',
            'maxlength':'16',
            'minlength':'6',
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder':'you@example.com',
            
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-input',
            'placeholder':'********',
            'maxlength':'22',
            'minlength':'8',
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'form-input',
            'placeholder':'********',
            'maxlength':'22',
            'minlength':'8',
        })
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname','lastname','phone','address','city','profile_pic']







class MyCustomSignupForm(SignupForm):

    def save(self, request):
        print('hehee')
        user = super(MyCustomSignupForm, self).save(request)
        print(user)
        return user

class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        print("Lo")
        return super(MyCustomLoginForm, self).login(*args, **kwargs)