# Generated by Django 5.2.1 on 2025-06-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_booking_userservicebooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='userservicebooking',
            name='city',
            field=models.CharField(default='city_name', max_length=50),
        ),
    ]
