from .models import Feedback
from django.forms import ModelForm
from django import forms


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
    