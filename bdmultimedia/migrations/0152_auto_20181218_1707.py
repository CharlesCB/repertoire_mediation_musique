# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 22:07
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0151_auto_20181218_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='outil',
            name='action',
            field=multiselectfield.db.fields.MultiSelectField(choices=[("D'e\u0301ducation musicale", "D'e\u0301ducation musicale"), ('De de\u0301veloppement de public', 'De de\u0301veloppement de public'), ('Publicitaire et promotionnelle', 'Publicitaire et promotionnelle'), ('De me\u0301diation de la musique', 'De me\u0301diation de la musique'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Cet outil sert une action (plusieurs choix possibles)'),
        ),
        migrations.AddField(
            model_name='outil',
            name='public_cible',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pas de public cible', 'Pas de public cible'), ('Nourisson et petite enfance (0 a\u0300 3 ans)', 'Nourisson et petite enfance (0 a\u0300 3 ans)'), ('Enfants (4 a\u0300 12 ans)', 'Enfants (4 a\u0300 12 ans)'), ('Adolescents (13 a\u0300 16 ans)', 'Adolescents (13 a\u0300 16 ans)'), ('Adulescents (16 a\u0300 18 ans)', 'Adulescents (16 a\u0300 18 ans)'), ('Jeunes actifs (19 a\u0300 25 ans)', 'Jeunes actifs (19 a\u0300 25 ans)'), ('Actifs (25 a\u0300 65 ans)', 'Actifs (25 a\u0300 65 ans)'), ('Retraite\u0301s -(plus de 65 ans)', 'Retraite\u0301s -(plus de 65 ans)')], max_length=300, null=True, verbose_name="Quelle est la tranche d'a\u0302ge du public cible de cet outil ?"),
        ),
    ]
