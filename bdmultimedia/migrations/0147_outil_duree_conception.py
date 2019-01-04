# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0146_auto_20181217_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='outil',
            name='duree_conception',
            field=models.CharField(choices=[('Un mois ou moins', 'Un mois ou moins'), ('Entre deux et six mois', 'Entre deux et six mois'), ('Entre six mois et un an', 'Entre six mois et un an'), ('Entre deux et cinq ans', 'Entre deux et cinq ans'), ('Plus de cinq ans', 'Plus de cinq ans'), ('De fac\u0327on permanente', 'De fac\u0327on permanente')], max_length=50, null=True, verbose_name='La conception du contenu de ce outil a e\u0301te\u0301 de'),
        ),
    ]
