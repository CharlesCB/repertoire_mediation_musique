# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0118_remove_outil_humain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='animaux',
        ),
        migrations.RemoveField(
            model_name='outil',
            name='instr_anime',
        ),
        migrations.RemoveField(
            model_name='outil',
            name='pers_anime',
        ),
    ]