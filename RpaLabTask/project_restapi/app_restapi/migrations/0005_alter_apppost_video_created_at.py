# Generated by Django 4.0.4 on 2022-07-22 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restapi', '0004_rename_post_by_apppost_video_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppost',
            name='video_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 11, 59, 56, 257096)),
        ),
    ]
