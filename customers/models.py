from sre_constants import MAX_UNTIL
from django.db import models
from django.core.validators import *
from django.core import validators
from professionals.models import Service
from django.contrib.auth.models import User

# Create your models here.
class Feedback(models.Model):
    user =models.ForeignKey(User, models.CASCADE, null=True)
    service=models.ForeignKey(Service, models.CASCADE, null=True)
    rating = models.IntegerField(null=True)
    subject = models.CharField(max_length=100, null=True)
    service_feedback = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.user