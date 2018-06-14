# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-17 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0125_auto_20180515_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='depouillement_date',
            field=models.DateField(null=True, verbose_name='R.12 Date du d\xe9pouillement'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='mise_en_ligne_date',
            field=models.DateField(help_text='Si seule l\u2019ann\xe9e de mise en ligne est disponible entrer la date de mise en ligne au 1er janvier de l\u2019ann\xe9e concern\xe9e', null=True, verbose_name='R.11 Date de la mise en ligne'),
        ),
    ]
