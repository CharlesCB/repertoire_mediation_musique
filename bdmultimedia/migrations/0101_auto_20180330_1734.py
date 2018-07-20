# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-30 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0100_auto_20180330_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='ensemble_thematique',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=4, verbose_name="R.3.1 Ce dispositif fait-il partie d'un ensemble th\xe9matique du m\xeame type? (regroup\xe9 par l'organisme producteur)"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='malentendants',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=200, verbose_name='S.24.1 Ce dispositif est-il accessible aux malentendants (Sous titrage, language des signes)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='malvoyants',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=200, verbose_name='S.24.2 Ce dispositif est-il accessible aux malvoyants (audiodescription)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='producteur_type',
            field=models.ManyToManyField(to='bdmultimedia.ProdType', verbose_name='R.4 Qui est le producteur de ce dispositif?'),
        ),
    ]