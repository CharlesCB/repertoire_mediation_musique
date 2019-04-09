# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-08 22:22
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0160_auto_20190401_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='outil',
            name='chant_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Chant', 'Chant'), ('Chanson', 'Chanson'), ('Hymnes nationaux ou sportifs', 'Hymnes nationaux ou sportifs')], max_length=42),
        ),
        migrations.AddField(
            model_name='outil',
            name='chorale_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Motet', 'Motet'), ('Madrigal', 'Madrigal')], max_length=14, verbose_name='Musique chorale. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='classique_moyen',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Musique de danse', 'Musique de danse'), ('Musique sacr\xe9e', 'Musique sacr\xe9e'), ('Musique chorale', 'Musique chorale'), ('Voix seule accompagn\xe9e', 'Voix seule accompagn\xe9e'), ('Op\xe9ra', 'Op\xe9ra'), ('Musique symphonique', 'Musique symphonique'), ('Musique de chambre', 'Musique de chambre'), ('\xc9lectroacoustique', '\xc9lectroacoustique'), ('Autre musique instrumentale', 'Autre musique instrumentale')], max_length=161, verbose_name='Musique classique. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='danse_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Ballet', 'Ballet'), ('Com\xe9die ballet', 'Com\xe9die ballet'), ('Danse', 'Danse'), ('Suite de danse', 'Suite de danse')], max_length=42, verbose_name='Musique de danse. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='genre_large',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Musique populaire', 'Musique populaire'), ('Musique classique et contemporaine', 'Musique classique et contemporaine'), ("Musique \xe0 l'image", "Musique \xe0 l'image"), ('Pas de genre \xe9voqu\xe9', 'Pas de genre \xe9voqu\xe9')], max_length=90, null=True, verbose_name='M.25.4 Parle-t-on du genre musical, si oui pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='image_moyen',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Musique de jeu vid\xe9o', 'Musique de jeu vid\xe9o'), ('Musique de film', 'Musique de film')], max_length=36, verbose_name="Musique \xe0 l'image. Si possible, pr\xe9cisez."),
        ),
        migrations.AddField(
            model_name='outil',
            name='opera_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Op\xe9ra', 'Op\xe9ra'), ('Semi-Op\xe9ra', 'Semi-Op\xe9ra'), ('Op\xe9rette', 'Op\xe9rette'), ('Grand op\xe9ra fran\xe7ais', 'Grand op\xe9ra fran\xe7ais'), ('Op\xe9ra-comique et Singspiel', 'Op\xe9ra-comique et Singspiel'), ('Ouverture', 'Ouverture')], max_length=83, verbose_name='Opera. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='pop_moyen',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Hip-Hop/Rap', 'Hip-Hop/Rap'), ('Chant, chanson hymne', 'Chant, chanson hymne'), ('\xc9lectro/ Techno', '\xc9lectro/ Techno'), ('Pop', 'Pop'), ('Blues', 'Blues'), ('Disco', 'Disco'), ('Folk/Indie', 'Folk/Indie'), ('Jazz', 'Jazz'), ('Musiques du monde et trad.', 'Musiques du monde et trad.'), ('Rock', 'Rock'), ('R&B', 'R&B'), ('Soul/Gospel', 'Soul/Gospel'), ('Western/Country', 'Western/Country'), ("Musique d'ambiance", "Musique d'ambiance"), ('Com\xe9die-musicale', 'Com\xe9die-musicale')], max_length=180, verbose_name='Musique populaire. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='sacree_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cantate', 'Cantate'), ('Oratorio', 'Oratorio'), ('Passion', 'Passion'), ('Messe', 'Messe'), ('Requiem', 'Requiem'), ('Motet', 'Motet')], max_length=44, verbose_name='Musique sacr\xe9e. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='symphonique_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Ouverture', 'Ouverture'), ('Symphonie', 'Symphonie'), ('Po\xe8me symphonique', 'Po\xe8me symphonique'), ('Concerto', 'Concerto')], max_length=46, verbose_name='Musique symphonique. Si possible, pr\xe9cisez.'),
        ),
        migrations.AddField(
            model_name='outil',
            name='voix_accompagnee_precis',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Romance', 'Romance'), ('Air de cour', 'Air de cour'), ('Lied et M\xe9lodie', 'Lied et M\xe9lodie')], max_length=35, verbose_name='Voix seule accompagn\xe9e. Si possible, pr\xe9cisez.'),
        ),
    ]