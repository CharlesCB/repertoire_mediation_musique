# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-14 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0132_auto_20180606_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='titre',
            field=models.CharField(db_index=True, max_length=200, verbose_name='R.1 Titre du dispositif'),
        ),
    ]
