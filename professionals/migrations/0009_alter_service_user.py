# Generated by Django 4.0 on 2022-02-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('professionals', '0008_service_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]