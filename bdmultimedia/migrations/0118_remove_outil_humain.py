# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0117_auto_20180513_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='humain',
        ),
    ]
