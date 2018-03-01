# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0041_auto_20170715_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='date_verif',
            field=models.DateField(blank=True, null=True, verbose_name='Date de la derni\xe8re v\xe9rification du lien'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='depouillement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date du d\xe9pouillement'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='duree',
            field=models.CharField(default='00:00:00', max_length=8, verbose_name='Dur\xe9e'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='mise_en_ligne_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date de la mise en ligne'),
        ),
    ]
