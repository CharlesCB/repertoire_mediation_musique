# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0121_auto_20180515_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='nb_animaux_total',
            field=models.CharField(help_text='Si le nombre exc\xe8de 11, \xe9crire "11 et plus"', max_length=50, null=True, verbose_name="St\xe9.41.1 Nombre d'animaux total"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='nb_pers_anime_total',
            field=models.CharField(help_text='Si le nombre exc\xe8de 11, \xe9crire "11 et plus"', max_length=50, null=True, verbose_name='St\xe9.40.1 Nombre de personnages anim\xe9s total'),
        ),
    ]
