# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0026_auto_20170617_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='date_verif',
            field=models.DateField(null=True, verbose_name='Date de la derni\xe8re v\xe9rification du lien'),
        ),
    ]