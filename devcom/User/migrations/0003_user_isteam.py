# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20170729_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isteam',
            field=models.IntegerField(default=1),
        ),
    ]