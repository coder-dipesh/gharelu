# Generated by Django 4.0 on 2022-02-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0006_alter_service_service_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_photo',
            field=models.FileField(default='static/images/no_image_service_watermarked.png', null=True, upload_to='static/uploads/service'),
        ),
    ]
