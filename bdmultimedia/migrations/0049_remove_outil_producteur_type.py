# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0048_auto_20170722_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='producteur_type',
        ),
    ]