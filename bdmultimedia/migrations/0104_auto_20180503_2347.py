# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-04 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0103_auto_20180424_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProducteurNom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Nom du producteur',
            },
        ),
        migrations.AlterField(
            model_name='outil',
            name='ensemble_thematique',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', help_text='On parle bien ici d\u2019un ensemble th\xe9matique et non pas d\u2019un regroupement par format (ex. vid\xe9o) ou par objectif (ex . ressource p\xe9dagogique). ', max_length=4, verbose_name="R.3.1 Ce dispositif fait-il partie d'un ensemble th\xe9matique du m\xeame type? (regroup\xe9 par l'organisme producteur)"),
        ),
        migrations.RemoveField(
            model_name='outil',
            name='producteur_nom',
        ),
        migrations.AlterField(
            model_name='outil',
            name='producteur_type',
            field=models.ManyToManyField(help_text='Attention : r\xe9pondre \xe0 cette question n\xe9cessite d\u2019aller v\xe9rifier les statuts des organismes impliqu\xe9s ou le titre auquel ils s\u2019impliquent. Exemple . L\u2019OSM peut agir en tant que producteur pour un concert ou au titre de diffuseur pour un autre \xe9v\xe8nement.', to='bdmultimedia.ProdType', verbose_name='R.4 Qui est le producteur de ce dispositif?'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='site',
            field=models.URLField(help_text='Attention, enlever la barre oblique \xab / \xbb \xe0 la fin de l\u2019URL www.osm.ca', verbose_name="R.3 URL d'acc\xe8s au site d'h\xe9bergement"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='url',
            field=models.CharField(help_text='Attention, enlever la barre oblique \xab / \xbb \xe0 la fin de l\u2019URL Ex. www.osm.ca/fr/matinees/#1488205065259-011decba-7105', max_length=200, unique=True, verbose_name="R.2 URL d'acc\xe8s direct"),
        ),
        migrations.AddField(
            model_name='outil',
            name='producteur_nom',
            field=models.ManyToManyField(to='bdmultimedia.ProducteurNom', verbose_name='R.5 Pr\xe9ciser le nom complet du/des producteur(s)'),
        ),
    ]