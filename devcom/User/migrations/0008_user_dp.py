# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20170730_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dp',
            field=models.CharField(default='/media/media/dp/pic_rOge5Ez.png', max_length=200, null=True),
        ),
    ]