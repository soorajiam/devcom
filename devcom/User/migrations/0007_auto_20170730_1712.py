# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20170730_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dp',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
