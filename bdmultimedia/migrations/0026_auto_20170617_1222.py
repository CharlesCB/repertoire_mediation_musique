# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0025_auto_20170617_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='date_verif',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date de la derni\xe8re v\xe9rification du lien'),
        ),
    ]