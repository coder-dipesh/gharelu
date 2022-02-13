from distutils.command.upload import upload
from django.db import models
from django.core.validators import *
from django.core import validators
from admins.models import Category
from django.contrib.auth.models import User

# Create your models here.


class Service(models.Model):

    SERVICE_LOCATION= (
        ('Kathmandu','Kathmandu'),
        ('Bhaktapur','Bhaktapur'),
        ('Lalitpur','Lalitpur')
    )
    service_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    service_description = models.TextField(null=True)
    service_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, )
    service_photo = models.FileField(upload_to='static/uploads/service',default='static/images/no_image_service_watermarked.png', null=True)
    service_price = models.IntegerField(null=True)
    service_location = models.CharField(max_length=100,choices=SERVICE_LOCATION,null=True)
    service_created_date = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.service_name