# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0003_auto_20170607_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElemMus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Faire une liste des \xe9l\xe9ments musicaux dont il est question',
            },
        ),
        migrations.AddField(
            model_name='outil',
            name='liste_experiences',
            field=models.ManyToManyField(to='bdmultimedia.ExpMus'),
        ),
        migrations.RemoveField(
            model_name='outil',
            name='experiences_musicales',
        ),
        migrations.AddField(
            model_name='outil',
            name='experiences_musicales',
            field=models.CharField(blank=True, choices=[('Non', 'Non'), ("Techniques d'\xe9coute", "Techniques d'\xe9coute"), ('Exp\xe9rience v\xe9cue', 'Exp\xe9rience v\xe9cue'), ('Le concert', 'Le concert'), ('Les r\xe9p\xe9titions (g\xe9n\xe9rale, raccord, etc.)', 'Les r\xe9p\xe9titions (g\xe9n\xe9rale, raccord, etc.)'), ('Autre', 'Autre')], max_length=200),
        ),
        migrations.AddField(
            model_name='outil',
            name='list_elements',
            field=models.ManyToManyField(to='bdmultimedia.ElemMus'),
        ),
    ]