# Generated by Django 2.2.6 on 2019-10-21 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy_app', '0006_trip_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='created_by',
        ),
    ]