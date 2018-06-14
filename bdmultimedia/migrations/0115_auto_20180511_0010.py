# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-11 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0114_auto_20180510_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='role_evolution',
            field=models.ManyToManyField(to='bdmultimedia.RoleEvolution', verbose_name="M.27.3 Parle-t-on du r\xf4le et de l'\xe9volution du [m\xe9tier li\xe9s \xe0 la musique pr\xe9cisez]"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='site',
            field=models.CharField(help_text='Attention, enlever la barre oblique \xab / \xbb \xe0 la fin de l\u2019URL www.osm.ca. <br> Si le dispositif est une vid\xe9o d\u2019un-e YouTubeur-e, indiquer le lien vers sa cha\xeene YouTube.', max_length=200, verbose_name="R.3 URL d'acc\xe8s au site d'h\xe9bergement"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='temps_mus',
            field=models.CharField(default='00:00:00', help_text='ddv = dur\xe9e d\u2019\xe9coute variable. Concerne les dispositifs qui allient texte et vid\xe9o. La dur\xe9e d\u2019\xe9coute est variable puisque les utilisateurs peuvent d\xe9cider, ou non, de regarder les vid\xe9os.<br> 00.00.00 =  signifie qu\u2019il y a bien du son dans le dispositif.<br> nsp signifie qu\u2019il n\u2019y a pas de son dans le dispositif.', max_length=8, verbose_name='PM.30 Temps de musique seule (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='temps_mus_par',
            field=models.CharField(default='00:00:00', help_text="ddv = dur\xe9e d\u2019\xe9coute variable. Concerne les dispositifs qui allient texte et vid\xe9o. La dur\xe9e d\u2019\xe9coute est variable puisque les utilisateurs peuvent d\xe9cider, ou non, de regarder les vid\xe9os.<br> nsp = ne s'applique pas", max_length=8, verbose_name='PM.32 Temps de parole et musique superpos\xe9es (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='temps_par',
            field=models.CharField(default='00:00:00', help_text="ddv = dur\xe9e d\u2019\xe9coute variable. Concerne les dispositifs qui allient texte et vid\xe9o. La dur\xe9e d\u2019\xe9coute est variable puisque les utilisateurs peuvent d\xe9cider, ou non, de regarder les vid\xe9os. <br> nsp = ne s'applique pas", max_length=8, verbose_name='PM.31 Temps de parole seule (hh:mm:ss)'),
        ),
    ]
