# Generated by Django 5.2.3 on 2025-06-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_userservicebooking_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='assigned',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
