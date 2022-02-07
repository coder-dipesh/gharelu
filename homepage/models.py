from django.db import models
from django.core import validators


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2)])
    product_feedback = models.TextField()

    def __str__(self):
        return self.product_feedback
