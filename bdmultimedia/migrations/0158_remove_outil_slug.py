# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0157_auto_20190109_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='slug',
        ),
    ]
