# Generated by Django 3.0.7 on 2020-08-24 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200824_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appoint_date_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appoint_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]