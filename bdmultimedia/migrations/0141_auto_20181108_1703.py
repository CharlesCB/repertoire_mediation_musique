# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0140_auto_20181024_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='outil',
            name='organologie',
            field=models.ManyToManyField(db_index=True, default=6, to='bdmultimedia.Organologie', verbose_name='M.27.4 Parle-t-on d\u2019organologie?'),
        ),
    ]