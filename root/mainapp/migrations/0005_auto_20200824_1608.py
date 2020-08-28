# Generated by Django 3.0.7 on 2020-08-24 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200824_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appoint_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appoint_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appoint_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
