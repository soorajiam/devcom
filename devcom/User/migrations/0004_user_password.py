# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_user_isteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=100),
            preserve_default=False,
        ),
    ]