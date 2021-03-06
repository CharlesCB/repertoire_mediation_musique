# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 15:02
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0020_auto_20170613_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outil',
            name='elements_socio',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ('Vie du compositeur, interpr\xe8te, d\xe9dica\xe7aire, m\xe9c\xe8ne', 'Vie du compositeur, interpr\xe8te, d\xe9dica\xe7aire, m\xe9c\xe8ne'), ('Organologie', 'Organologie'), ('Lutherie', 'Lutherie'), ('\xc9volution de la profession', '\xc9volution de la profession'), ('Conventions', 'Conventions'), ('Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)', 'Epoques dat\xe9es (ex. les dates du Romantisme ou r\xe9f\xe9rence au 18\xe8)'), ('Oeuvres (\xe0 titre documentaires)', 'Oeuvres (\xe0 titre documentaires)'), ('Contexte de production', 'Contexte de production'), ('Contexte de r\xe9ception', 'Contexte de r\xe9ception'), ('Contexte de cr\xe9ation (au sens de "la premi\xe8re")', 'Contexte de cr\xe9ation (au sens de "la premi\xe8re")'), ('Autre', 'Autre')], max_length=200, verbose_name='El\xe9ments socioculturels et historiques'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocaion_litteraire',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ('Texte oral', 'Texte oral'), ('Texte \xe9crit', 'Texte \xe9crit'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation litt\xe9raire'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocaion_plastique',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ('Sculpture', 'Sculpture'), ('Installation', 'Instalation'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation plastique'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocation_autre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Aucune', 'Aucune'), ('Litt\xe9rature', 'Litt\xe9rature'), ('Danse', 'Danse'), ('Art plastiques', 'Art plastiques'), ('Th\xe9\xe2tre', 'Th\xe9\xe2tre'), ('Cin\xe9ma', 'Cin\xe9ma'), ('Arts num\xe9riques', 'Arts num\xe9riques'), ('Sports', 'Sports'), ('Neurosciences', 'Neurosciences'), ('Sciences physiques', 'Sciences physiques'), ('Architechture', 'Architechture'), ('Gastronomie', 'Gastronomie'), ('Cirque', 'Cirque'), ('Performance', 'Performance'), ('Anatomie', 'Anatomie'), ('Autre', 'Autre')], max_length=200, verbose_name='Autres disciplines \xe9voqu\xe9es'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='evocation_graphique',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ('Repr\xe9sentation graphique traditionnelle (partition + notes)', 'Repr\xe9sentation graphique traditionnelle (partition + notes)'), ("Repr\xe9sentation graphique traditionnelle augment\xe9e (Ex. les notes s'\xe9clairent quand on les entends", "Repr\xe9sentation graphique traditionnelle augment\xe9e (Ex. les notes s'\xe9clairent quand on les entends"), ('Repr\xe9sentation graphique traditionelle illustr\xe9e (Ex. les notes sont en fait des oiseaux sur les lignes de la port\xe9e)', 'Repr\xe9sentation graphique traditionelle illustr\xe9e (Ex. les notes sont en fait des oiseaux sur les lignes de la port\xe9e)'), ('Repr\xe9sentation graphique sch\xe9matis\xe9e (Ex. il y toujours un port\xe9e mais ce sont des courbes qui figurent la m\xe9lodie)', 'Repr\xe9sentation graphique sch\xe9matis\xe9e (Ex. il y toujours un port\xe9e mais ce sont des courbes qui figurent la m\xe9lodie)'), ('Repr\xe9sentation graphique symbolis\xe9e (Ex. des images anim\xe9es, cf. ratatouille!!)', 'Repr\xe9sentation graphique symbolis\xe9e (Ex. des images anim\xe9es, cf. ratatouille!!)'), ('Autre', 'Autre')], max_length=200, verbose_name='\xc9vocation graphique'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='experiences_musicales',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ("Techniques d'\xe9coute", "Techniques d'\xe9coute"), ('Exp\xe9rience v\xe9cue', 'Exp\xe9rience v\xe9cue'), ('Le concert', 'Le concert'), ('Les r\xe9p\xe9titions (g\xe9n\xe9rale, raccord, etc.)', 'Les r\xe9p\xe9titions (g\xe9n\xe9rale, raccord, etc.)'), ('Autre', 'Autre')], max_length=200),
        ),
        migrations.AlterField(
            model_name='outil',
            name='format',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ecrit (texte, dessin)', 'Ecrit (texte, dessin)'), ('Audio', 'Audio'), ('Audiovisuel', 'Audiovisuel'), ('Immersif', 'Immersif'), ('R\xe9alit\xe9 augment\xe9e', 'R\xe9alit\xe9 augment\xe9e'), ('Autre', 'Autre')], max_length=200, verbose_name="Format de l'outil"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='forme_narrative',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Entrevue', 'Entrevue'), ('Fiction', 'Fiction'), ("Synopsis (r\xe9cit fid\xe8le au programme de l'oeuvre)", "Synopsis (r\xe9cit fid\xe8le au programme de l'oeuvre)"), ('Web-s\xe9rie (plusieurs occurences qui ont un lien entre elles)', 'Web-s\xe9rie (plusieurs occurences qui ont un lien entre elles)'), ('Animation', 'Animation'), ('Art et essai', 'Art et essai'), ('Vulgarisation', 'Vulgarisation'), ('Creative commons (sur le mod\xe8le wiki)', 'Creative commons (sur le mod\xe8le wiki)'), ('Reportage', 'Reportage'), ('Jeu', 'Jeu'), ('Autre', 'Autre')], max_length=200, verbose_name='Forme narrative g\xe9n\xe9rale'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='materiau_musical',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ('Son', 'Son'), ('Structure', 'Structure'), ('Language musical', 'Language musical'), ('Genre (op\xe9ra, symphonique)', 'Genre (op\xe9ra, symphonique)'), ('Style (Classique, Romantique, Contemporain)', 'Style (Classique, Romantique, Contemporain)'), ('Autre', 'Autre')], max_length=200, verbose_name='Mat\xe9riau musical'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='mode_hebergement',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Youtube / Vimeo, etc..', 'Youtube / Vimeo, etc..'), ('Portail institutionnel', 'Portail institutionnel'), ('R\xe9seau social', 'R\xe9seau social'), ('Cloud', 'Cloud'), ('Autre', 'Autre')], max_length=200, verbose_name="Mode d'h\xe9bergement sur la toile"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='narration_langue',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Fran\xe7ais', 'Fran\xe7ais'), ('Anglais', 'Anglais'), ('Allemand', 'Allemand'), ('Portugais', 'Portugais'), ('Autre', 'Autre')], max_length=200, verbose_name='Langue de la narration'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='pratique_musicale',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Non', 'Non'), ('Techniques instrumentales (mode de production du son)', 'Techniques instrumentales (mode de production du son)'), ("Activit\xe9 du musicien, du compositeur, de l'interpr\xe8te, du luthier etc.", "Activit\xe9 du musicien, du compositeur, de l'interpr\xe8te, du luthier etc."), ('Pratique professionnelle', 'Pratique professionnelle'), ('Pratique amateur', 'Pratique amateur'), ('Autre', 'Autre')], max_length=200, verbose_name='Pratique musicale'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='solicitation_autre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Lire', 'Lire'), ('Regarder', 'Regarder'), ('Bricoler', 'Bricoler'), ('Jouer (au sens ludique)', 'Jouer (au sens ludique)'), ('\xc9crire', '\xc9crire'), ('Autre', 'Autre')], max_length=200, verbose_name="En g\xe9n\xe9ral (hors musique) comment sollicite-t-on l'usager?"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='solicitation_musicale',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Interpr\xe9ter', 'Interpr\xe9ter'), ('Reproduire', 'Reproduire'), ('\xc9couter', '\xc9couter'), ('Inventer/composer/improviser', 'Inventer/composer/improviser'), ('Lire', 'Lire'), ('Regarder', 'Regarder'), ('Autre', 'Autre')], max_length=200, verbose_name="Comment sollicite-t-on musicalement l'usager?"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='sonore_valeur',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Premier plan', 'Premier Plan'), ('Arri\xe8re plan', 'Arri\xe8re plan'), ('Alternance', 'Alternance'), ('Aucune', 'Aucune'), ('Autre', 'Autre')], max_length=200, verbose_name='Mise en valeur du sonore'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='sous_titre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pas de sous titrage', 'Pas de sous titrage'), ('Fran\xe7ais', 'Fran\xe7ais'), ('Anglais', 'Anglais'), ('Allemand', 'Allemand'), ('Portugais', 'Portugais'), ('Autre', 'Autre')], max_length=200, verbose_name='Sous-titrage'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='support_diffusion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ordinateur', 'Ordinateur'), ('Smartphone', 'Smartphone'), ('Tablette', 'Tablette'), ('Lunettes 3D', 'Lunettes 3D'), ('Consoles de JV', 'Consoles de JV'), ('DVD', 'DVD'), ('CD', 'CD'), ('Autre', 'Autre')], max_length=200, verbose_name='Support de diffusion'),
        ),
    ]
