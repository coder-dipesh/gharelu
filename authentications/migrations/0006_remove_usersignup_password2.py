# Generated by Django 4.0 on 2021-12-21 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0005_rename_user_usersignup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersignup',
            name='password2',
        ),
    ]
