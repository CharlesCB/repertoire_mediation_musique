# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-07 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0110_auto_20180507_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='page_outil',
            field=models.BooleanField(default=False, verbose_name='Afficher directement une page qui fait office de dispositif'),
        ),
    ]