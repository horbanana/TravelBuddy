# Generated by Django 2.2.6 on 2019-10-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy_app', '0003_auto_20191021_0133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='traveler',
            new_name='creator',
        ),
    ]
