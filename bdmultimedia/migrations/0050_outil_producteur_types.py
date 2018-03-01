# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 18:43
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0049_remove_outil_producteur_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='outil',
            name='producteur_types',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Particulier', 'Particulier'), ('Organisme de diffusion (OSM, Festival)', 'Organisme de diffusion (OSM, Festival)'), ('Organisme de formation professionnelle (CQM, ARIAM, CFMI)', 'Organisme de formation professionnelle (CQM, ARIAM, CFMI)'), ('Groupe de recherche (P2M, Groupe de recherche sur la m\xe9diation culturelle)', 'Groupe de recherche (P2M, Groupe de recherche sur la m\xe9diation culturelle)'), ('Organismes \xe9ducatif (Ecole de musique, TEDX)', 'Organismes \xe9ducatif (Ecole de musique, TEDX)'), ('Autre', 'Autre')], max_length=234, verbose_name='Producteurs'),
        ),
    ]
