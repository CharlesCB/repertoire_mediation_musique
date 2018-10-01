# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-05 13:53
from __future__ import unicode_literals

import bdmultimedia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0144_auto_20180802_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', bdmultimedia.models.CustomDateField(verbose_name='TEST DATE')),
            ],
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_neutre',
            field=models.ManyToManyField(db_index=True, to='bdmultimedia.RoleHumainNeutre', verbose_name='St\xe9.39.4 R\xf4le des ind\xe9termin\xe9s'),
        ),
    ]
