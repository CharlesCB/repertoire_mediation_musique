# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-04 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0105_auto_20180503_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='materiel_imprimer',
            field=models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=200, verbose_name='R.13.1 Le dispositif comprend-il du mat\xe9riel \xe0 imprimer (ex. livret en pdf) ?'),
        ),
    ]
