from django.forms import ModelForm
from professionals.models import Service


class ServiceForm(ModelForm):
  class Meta:
    model = Service
    fields = "__all__"
    exclude = ['user']