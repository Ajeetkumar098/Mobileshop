# Generated by Django 4.1.6 on 2023-05-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0005_contact_us_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='permission',
            field=models.BooleanField(default=False),
        ),
    ]
