from .models import Category
from django.forms import ModelForm



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


