from django.db import models
from pydantic import validator


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100, validators=[validator.MinLengthValidator(2)])
    product_feedback = models.TextField()

    def __str__(self):
        return self.product_feedback

