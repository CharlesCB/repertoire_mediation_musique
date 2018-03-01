# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-11 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0077_auto_20180211_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='evocation_autre',
            field=models.ManyToManyField(to='bdmultimedia.EvocationAutre', verbose_name='I.37 Autres disciplines \xe9voqu\xe9es'),
        ),
        migrations.RemoveField(
            model_name='outil',
            name='notion_concepts',
        ),
        migrations.AddField(
            model_name='outil',
            name='notion_concepts',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non'), ('Nsp', "Ne s'applique pas")], default='Nsp', max_length=50, verbose_name='\xc0 partir de quelle notion? - Notions communes (luminosit\xe9, transparence, vitesse, mouvement)'),
        ),
    ]