from homepage.views import review
from .models import Category
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class review(ModelForm):
    class Meta:
        model = review
        fields = "__all__"
