# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0032_outil_notion_concepts'),
    ]

    operations = [
        migrations.AddField(
            model_name='outil',
            name='notion_pratiques',
            field=models.ManyToManyField(to='bdmultimedia.NotPratique', verbose_name='Pratique (processus de cr\xe9ation)'),
        ),
    ]
