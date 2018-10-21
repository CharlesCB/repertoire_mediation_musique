# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-19 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0146_delete_customtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='mise_en_ligne_date',
            field=models.DateField(blank=True, help_text="Si seule l\u2019ann\xe9e de mise en ligne est disponible entrer la date de mise en ligne au 1er janvier de l\u2019ann\xe9e concern\xe9e. Si la date n'est pas disponible, laisser vide.", null=True, verbose_name='R.11 Date de la mise en ligne'),
        ),
    ]