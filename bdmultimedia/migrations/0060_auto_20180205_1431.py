# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-05 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0059_auto_20180205_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='site',
            field=models.URLField(help_text='ex. site de la Philharmonie de Paris', verbose_name="Chemin d'acc\xe8s au site d'h\xe9bergement"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='url',
            field=models.CharField(help_text="Dernier URL \xe0 suivre pour ateindre l'outil - nsp = ne s'applique pas", max_length=200, unique=True, verbose_name="Chemin d'acc\xe8s direct"),
        ),
    ]