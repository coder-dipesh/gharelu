# Generated by Django 4.0 on 2022-01-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0018_alter_userotp_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
