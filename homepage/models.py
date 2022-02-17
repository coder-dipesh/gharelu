from django.db import models
from django.contrib.auth.models import User
from professionals.models import Service
from django.core.validators import *
# Create your models here.

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
    contact_address = models.CharField(max_length=200, null=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email



