from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authentications.models import UserSignUp

class CreateUserForm(forms.ModelForm):
    class Meta:
        
        model = UserSignUp
        fields = '__all__'
        widgets = {
            'password1' : forms.PasswordInput(),
        }

        # fields = ['username','email','password1','password2']
