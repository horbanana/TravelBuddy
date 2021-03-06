# Generated by Django 2.2.6 on 2019-10-21 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy_app', '0002_auto_20191021_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='reated_at',
            new_name='created_at',
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=225)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('plan', models.TextField()),
                ('join', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel', to='travel_buddy_app.User')),
            ],
        ),
    ]
