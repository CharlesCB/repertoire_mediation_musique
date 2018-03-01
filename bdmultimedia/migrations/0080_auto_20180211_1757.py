# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-11 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0079_auto_20180211_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleFemmes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Role des femmes',
            },
        ),
        migrations.CreateModel(
            name='RoleHumainNeutre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Role des humain neutre',
            },
        ),
        migrations.AlterModelOptions(
            name='rolehomme',
            options={'verbose_name': 'Role des hommes'},
        ),
        migrations.AddField(
            model_name='outil',
            name='role_humain_femme',
            field=models.ManyToManyField(to='bdmultimedia.RoleFemmes', verbose_name='R\xf4le des femmes'),
        ),
        migrations.AddField(
            model_name='outil',
            name='role_humain_neutre',
            field=models.ManyToManyField(to='bdmultimedia.RoleHumainNeutre', verbose_name='R\xf4le des neutres'),
        ),
    ]
