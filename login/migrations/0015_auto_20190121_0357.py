# Generated by Django 2.0.10 on 2019-01-21 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20190121_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 3, 57, 35, 484344)),
        ),
        migrations.AlterField(
            model_name='user',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 3, 57, 35, 484344)),
        ),
    ]
