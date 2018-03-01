# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-12 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0083_auto_20180211_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='role_animaux_femme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleAnimauxFemmes', verbose_name='St\xe9.41.3 R\xf4le des animaux femelles'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_animaux_homme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleAnimauxHomme', verbose_name='St\xe9.41.2 R\xf4le des animaux m\xe2les'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_animaux_neutre',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleAnimauxNeutre', verbose_name='St\xe9.41.4 R\xf4le des animaux neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_femme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleFemmes', verbose_name='St\xe9.39.2 R\xf4le des femmes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_homme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleHomme', verbose_name='St\xe9.39.3 R\xf4le des hommes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_humain_neutre',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleHumainNeutre', verbose_name='St\xe9.39.4 R\xf4le des indetermin\xe9s'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_instr_anime_femme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleInstrFemmes', verbose_name='St\xe9.42.3 R\xf4le des instruments anthropomorphes f\xe9minins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_instr_anime_homme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleInstrHomme', verbose_name='St\xe9.42.2 R\xf4le des instruments anthropomorphes masculins'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_instr_anime_neutre',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RoleInstrNeutre', verbose_name='St\xe9.42.4 R\xf4le des instruments anthropomorphes neutres'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_anime_femme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RolePersAnimFemmes', verbose_name='St\xe9.40.3 R\xf4le des personnages anim\xe9s femmes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_anime_homme',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RolePersAnimHomme', verbose_name='St\xe9.40.2 R\xf4le des personnages anim\xe9s hommes'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='role_pers_anime_neutre',
            field=models.ManyToManyField(blank=True, to='bdmultimedia.RolePersAnimNeutre', verbose_name='St\xe9.40.4 R\xf4le des personnages anim\xe9s neutres'),
        ),
    ]