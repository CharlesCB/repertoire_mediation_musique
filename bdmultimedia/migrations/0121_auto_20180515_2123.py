# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0120_auto_20180515_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='nb_humains_total',
            field=models.CharField(help_text='Si le nombre exc\xe8de 11, \xe9crire "11 et plus"', max_length=50, verbose_name="St\xe9.39.1 Nombre d'humains total"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='nb_pages',
            field=models.CharField(help_text="Correspond au nombre de page web sur lesquelles se d\xe9cline le  dispositif. Nsp = ne s'applique pas. Si plus que 20 pages, inscrire : plus de 20 pages", max_length=50, null=True, verbose_name='R.10 Nombre de pages'),
        ),
    ]
