# Generated by Django 4.0 on 2022-02-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
