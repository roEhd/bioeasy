# Generated by Django 3.1 on 2020-09-10 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperEasyapp', '0002_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 20, 38, 6, 183820)),
        ),
    ]