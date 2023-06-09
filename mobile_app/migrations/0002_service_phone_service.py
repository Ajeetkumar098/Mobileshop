# Generated by Django 4.1.6 on 2023-04-21 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='service',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mobile_app.service'),
            preserve_default=False,
        ),
    ]
