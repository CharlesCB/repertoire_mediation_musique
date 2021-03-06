# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0030_auto_20170617_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Notion Concept',
            },
        ),
        migrations.CreateModel(
            name='NotExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Notion Exp\xe9riences',
            },
        ),
        migrations.CreateModel(
            name='NotPratique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Notion pratique',
            },
        ),
        migrations.RemoveField(
            model_name='outil',
            name='notion_concepts',
        ),
        migrations.RemoveField(
            model_name='outil',
            name='notion_experiences',
        ),
        migrations.RemoveField(
            model_name='outil',
            name='notion_pratique',
        ),
    ]
