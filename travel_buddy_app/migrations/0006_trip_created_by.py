# Generated by Django 2.2.6 on 2019-10-21 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy_app', '0005_auto_20191021_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_byCurrentUser', to='travel_buddy_app.User'),
            preserve_default=False,
        ),
    ]
