# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0004_auto_20170608_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='list_elements',
        ),
        migrations.AddField(
            model_name='outil',
            name='elements_socio',
            field=models.CharField(blank=True, choices=[('Non', 'Non'), ('Vie du compositeur, interpr\xe8te, d\xe9dica\xe7aire, m\xe9c\xe8ne', 'Vie du compositeur, interpr\xe8te, d\xe9dica\xe7aire, m\xe9c\xe8ne'), ('Organologie', 'Organologie'), ('Lutherie', 'Lutherie'), ('\xc9volution de la profession', '\xc9volution de la profession'), ('Conventions', 'Conventions'), ('Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)', 'Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)'), ('Oeuvres (\xe0 titre documentaires)', 'Oeuvres (\xe0 titre documentaires)'), ('Contexte de production', 'Contexte de production'), ('Contexte de r\xe9ception', 'Contexte de r\xe9ception'), ('Contexte de cr\xe9ation (au sens de "la premi\xe8re")', 'Contexte de cr\xe9ation (au sens de "la premi\xe8re")'), ('Autre', 'Autre')], max_length=200, verbose_name='El\xe9ments socioculturels et historiques'),
        ),
        migrations.AddField(
            model_name='outil',
            name='liste_materiau',
            field=models.ManyToManyField(to='bdmultimedia.ElemMus', verbose_name='Faire une liste des \xe9l\xe9ments musicaux dont il est question'),
        ),
    ]
