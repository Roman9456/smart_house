# Generated by Django 4.2.5 on 2023-10-15 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='image',
        ),
    ]
