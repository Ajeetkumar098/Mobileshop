# Generated by Django 4.1.6 on 2023-04-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0003_alter_phone_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='Description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]