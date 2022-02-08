from django.db import models
from django.core.validators import *
from django.core import validators
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_description = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

# class Feedback(models.Model):
#     name = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
#     product_feedback = models.TextField()

#     def __str__(self):
#         return self.feedback

