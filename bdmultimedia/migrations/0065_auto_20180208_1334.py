# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-08 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0064_auto_20180205_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='interface_type',
        ),
        migrations.AddField(
            model_name='outil',
            name='interface',
            field=models.CharField(choices=[('Simple consultation', 'Collaborative'), ('Interactive', 'Interactive'), ('Neutre', 'Neutre')], max_length=200, null=True, verbose_name="Type d'interface"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='depouillement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date du d\xe9pouillement'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='mise_en_ligne_date',
            field=models.DateField(blank=True, help_text='laisser vide si non disponible', null=True, verbose_name='Date de la mise en ligne'),
        ),
    ]