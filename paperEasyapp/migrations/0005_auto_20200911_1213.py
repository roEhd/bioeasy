# Generated by Django 3.1 on 2020-09-11 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperEasyapp', '0004_auto_20200911_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 12, 13, 20, 229852)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 12, 13, 20, 228830)),
        ),
    ]