# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(null=True, upload_to='media/dp'),
        ),
    ]
