# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-11 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0113_contreexemple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='commentaire_nombre',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='R.16 Nombre de commentaires'),
        ),
    ]
