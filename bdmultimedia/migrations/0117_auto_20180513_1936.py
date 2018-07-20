# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-13 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0116_auto_20180511_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contreexemple',
            name='contexte',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='evocation_autre',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='evocation_graphique',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='evocation_plastique',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='exemples_notions_interdisciplinaires',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='experience_musicale',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='format',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='forme_narrative',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='genre_musical',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='language_musical',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='mode_consultation',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='mode_hebergement',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='narration_langue',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='orchestration',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='producteur_type',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_animaux_femme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_animaux_homme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_animaux_neutre',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_evolution',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_humain_femme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_humain_homme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_humain_neutre',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_instr_anime_femme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_instr_anime_homme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_instr_anime_neutre',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_pers_anime_femme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_pers_anime_homme',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='role_pers_anime_neutre',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='sollicitation_generale',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='sollicitation_musicale',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='sous_titre',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='structure',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='style_musical',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='support_diffusion',
        ),
        migrations.RemoveField(
            model_name='contreexemple',
            name='utilisateur',
        ),
        migrations.AlterField(
            model_name='outil',
            name='nb_pages',
            field=models.PositiveIntegerField(default=0, help_text='Correspond au nombre de page web sur lesquelles se d\xe9cline le  dispositif .', null=True, verbose_name='R.10 Nombre de pages'),
        ),
        migrations.DeleteModel(
            name='ContreExemple',
        ),
    ]