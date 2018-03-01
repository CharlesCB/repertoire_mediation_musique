# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 19:34
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0052_auto_20170723_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='elements_socio',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Non', 'Non'), ('Vie du compositeur; interpr\xe8te; d\xe9dica\xe7aire; m\xe9c\xe8ne', 'Vie du compositeur; interpr\xe8te; d\xe9dica\xe7aire; m\xe9c\xe8ne'), ('Organologie', 'Organologie'), ('Lutherie', 'Lutherie'), ('\xc9volution de la profession', '\xc9volution de la profession'), ('Conventions', 'Conventions'), ('Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)', 'Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)'), ('Oeuvres (\xe0 titre documentaires)', 'Oeuvres (\xe0 titre documentaires)'), ('Contexte de production', 'Contexte de production'), ('Contexte de r\xe9ception', 'Contexte de r\xe9ception'), ('Contexte de cr\xe9ation (au sens de "la premi\xe8re")', 'Contexte de cr\xe9ation (au sens de "la premi\xe8re")'), ('Autre', 'Autre')], max_length=200, verbose_name='Contenu musical - el\xe9ments socioculturels et historiques'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocation_graphique',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Non', 'Non'), ('Repr\xe9sentation graphique traditionnelle (partition + notes)', 'Repr\xe9sentation graphique traditionnelle (partition + notes)'), ("Repr\xe9sentation graphique traditionnelle augment\xe9e (Ex. les notes s'\xe9clairent quand on les entends)", "Repr\xe9sentation graphique traditionnelle augment\xe9e (Ex. les notes s'\xe9clairent quand on les entends)"), ('Repr\xe9sentation graphique traditionelle illustr\xe9e (Ex. les notes sont en fait des oiseaux sur les lignes de la port\xe9e)', 'Repr\xe9sentation graphique traditionelle illustr\xe9e (Ex. les notes sont en fait des oiseaux sur les lignes de la port\xe9e)'), ('Repr\xe9sentation graphique sch\xe9matis\xe9e (Ex. il y toujours un port\xe9e mais ce sont des courbes qui figurent la m\xe9lodie)', 'Repr\xe9sentation graphique sch\xe9matis\xe9e (Ex. il y toujours un port\xe9e mais ce sont des courbes qui figurent la m\xe9lodie)'), ('Repr\xe9sentation graphique symbolis\xe9e (Ex. des images anim\xe9es; cf. ratatouille!!)', 'Repr\xe9sentation graphique symbolis\xe9e (Ex. des images anim\xe9es; cf. ratatouille!!)'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation graphique'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='experiences_musicales',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Non', 'Non'), ("Techniques d'\xe9coute", "Techniques d'\xe9coute"), ('Exp\xe9rience v\xe9cue', 'Exp\xe9rience v\xe9cue'), ('Le concert', 'Le concert'), ('Les r\xe9p\xe9titions (g\xe9n\xe9rale; raccord; etc.)', 'Les r\xe9p\xe9titions (g\xe9n\xe9rale; raccord; etc.)'), ('Autre', 'Autre')], max_length=200, verbose_name='Contenu musical - experiences musicales'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='format',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Ecrit (texte; dessin)', 'Ecrit (texte; dessin)'), ('Audio', 'Audio'), ('Audiovisuel', 'Audiovisuel'), ('Immersif', 'Immersif'), ('R\xe9alit\xe9 augment\xe9e', 'R\xe9alit\xe9 augment\xe9e'), ('Autre', 'Autre')], max_length=200, verbose_name="Format de l'outil"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='materiau_musical',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Non', 'Non'), ('Son', 'Son'), ('Structure', 'Structure'), ('Language musical', 'Language musical'), ('Genre (op\xe9ra; symphonique)', 'Genre (op\xe9ra; symphonique)'), ('Style (Classique; Romantique; Contemporain)', 'Style (Classique; Romantique; Contemporain)'), ('Autre', 'Autre')], max_length=200, verbose_name='Contenu musical - mat\xe9riau musical'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='mode_hebergement',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Youtube / Vimeo; etc..', 'Youtube / Vimeo; etc..'), ('Portail institutionnel', 'Portail institutionnel'), ('R\xe9seau social', 'R\xe9seau social'), ('Cloud', 'Cloud'), ('Autre', 'Autre')], max_length=200, verbose_name="Mode d'h\xe9bergement sur la toile"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='pratique_musicale',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Non', 'Non'), ('Techniques instrumentales (mode de production du son)', 'Techniques instrumentales (mode de production du son)'), ("Activit\xe9 du musicien; du compositeur; de l'interpr\xe8te; du luthier etc.", "Activit\xe9 du musicien; du compositeur; de l'interpr\xe8te; du luthier etc."), ('Pratique professionnelle', 'Pratique professionnelle'), ('Pratique amateur', 'Pratique amateur'), ('Autre', 'Autre')], max_length=200, verbose_name='Contenu musical - pratique musicale'),
        ),
    ]
