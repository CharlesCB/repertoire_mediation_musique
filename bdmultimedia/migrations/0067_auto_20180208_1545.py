# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-08 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0066_auto_20180208_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outil',
            name='autre_onglet',
        ),
        migrations.RemoveField(
            model_name='outil',
            name='quatrieme_onglet',
        ),
        migrations.AddField(
            model_name='outil',
            name='deux_onglet_autre',
            field=models.CharField(max_length=200, null=True, verbose_name='Si autre, pr\xe9cisez'),
        ),
        migrations.AddField(
            model_name='outil',
            name='prem_onglet_autre',
            field=models.CharField(max_length=200, null=True, verbose_name='Si autre, pr\xe9cisez'),
        ),
        migrations.AddField(
            model_name='outil',
            name='trois_onglet_autre',
            field=models.CharField(max_length=200, null=True, verbose_name='Si autre, pr\xe9cisez'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='commentaire_nombre',
            field=models.PositiveIntegerField(blank=True, help_text="Laisser vide si ne s'applique pas", null=True, verbose_name='Nombre de commentaires'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='deuxieme_onglet',
            field=models.CharField(choices=[("Ne s'applique pas", "Ne s'applique pas car l'outil \xe9tait disponible sur la page d'accueil"), ("On peut consulter l'outil directement sur cette deuxi\xe8me page", "On peut consulter l'outil directement sur cette deuxi\xe8me page"), ('Action culturelle', 'Action culturelle'), ('M\xe9diation', 'M\xe9diation'), ('\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que', '\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que'), ('Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental', 'Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental'), ('Pour tous les publics', 'Pour tout les publics'), ("L'orchestre et vous", "L'orchestre et vous"), ("Guide d'\xe9coute", "Guide d'\xe9coute"), ('Livret p\xe9dagogique', 'Livret p\xe9dagogique'), ('Pour les enseignants, \xe9coles, scolaires', 'Pour les enseignants, \xe9coles, scolaires'), ("Le nom de l'outil lui m\xeame", "Le nom de l'outil lui m\xeame (ex: 'La galerie symphonique')"), ('Ressources en ligne, ressources num\xe9riques, ressources', 'Ressources en ligne, ressources num\xe9riques, ressources'), ('Relatif \xe0 la programmation', 'Est relatif \xe0 la programmation \xe0 laquelle il fait r\xe9f\xe9rence (onglet du concert, titre du compositeur, etc.)'), ("Relatif au format de l'outil dont il s'agit", "Est relatif au format de l'outil dont il s'agit (Balado, vid\xe9o, playlist, web s\xe9rie, etc.)"), ('\xc0 propos', '\xc0 propos'), ('Voir et entendre', 'Voir et entendre'), ('Actualit\xe9s, news, nouveaut\xe9', 'Actualit\xe9, news, nouveaut\xe9'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Sous quel onglet du site est r\xe9f\xe9renc\xe9 cet outil - Deuxi\xe8me onglet \xe0 ouvrir'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='premier_onglet',
            field=models.CharField(choices=[("Ne s'applique pas", "Ne s'applique pas"), ("Disponible et consultable sur la page d'acc\xe8s", "L'outil est disponible et consultable sur la page d'acc\xe8s"), ('Action culturelle', 'Action culturelle'), ('M\xe9diation', 'M\xe9diation'), ('\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que', '\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que'), ('Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental', 'Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental'), ('Pour tous les publics', 'Pour tout les publics'), ("L'orchestre et vous", "L'orchestre et vous"), ("Guide d'\xe9coute", "Guide d'\xe9coute"), ('Livret p\xe9dagogique', 'Livret p\xe9dagogique'), ('Pour les enseignants, \xe9coles, scolaires', 'Pour les enseignants, \xe9coles, scolaires'), ("Le nom de l'outil lui m\xeame", "Le nom de l'outil lui m\xeame (ex: 'La galerie symphonique')"), ('Ressources en ligne, ressources num\xe9riques, ressources', 'Ressources en ligne, ressources num\xe9riques, ressources'), ('Relatif \xe0 la programmation', 'Est relatif \xe0 la programmation \xe0 laquelle il fait r\xe9f\xe9rence (onglet du concert, titre du compositeur, etc.)'), ("Relatif au format de l'outil dont il s'agit", "Est relatif au format de l'outil dont il s'agit (Balado, vid\xe9o, playlist, web s\xe9rie, etc.)"), ('\xc0 propos', '\xc0 propos'), ('Voir et entendre', 'Voir et entendre'), ('Actualit\xe9s, news, nouveaut\xe9', 'Actualit\xe9, news, nouveaut\xe9'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name="Quel est le PREMIER onglet \xe0 ouvrir pour trouver l'outil"),
        ),
        migrations.AlterField(
            model_name='outil',
            name='troisieme_onglet',
            field=models.CharField(choices=[("Ne s'applique pas", "Ne s'applique pas car l'outil \xe9tait disponible sur la deuxi\xe8me page"), ("On peut consulter l'outil directement sur cette troisi\xe8me page", "On peut consulter l'outil directement sur cette trois\xe8me page"), ('Action culturelle', 'Action culturelle'), ('M\xe9diation', 'M\xe9diation'), ('\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que', '\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que'), ('Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental', 'Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental'), ('Pour tous les publics', 'Pour tout les publics'), ("L'orchestre et vous", "L'orchestre et vous"), ("Guide d'\xe9coute", "Guide d'\xe9coute"), ('Livret p\xe9dagogique', 'Livret p\xe9dagogique'), ('Pour les enseignants, \xe9coles, scolaires', 'Pour les enseignants, \xe9coles, scolaires'), ("Le nom de l'outil lui m\xeame", "Le nom de l'outil lui m\xeame (ex: 'La galerie symphonique')"), ('Ressources en ligne, ressources num\xe9riques, ressources', 'Ressources en ligne, ressources num\xe9riques, ressources'), ('Relatif \xe0 la programmation', 'Est relatif \xe0 la programmation \xe0 laquelle il fait r\xe9f\xe9rence (onglet du concert, titre du compositeur, etc.)'), ("Relatif au format de l'outil dont il s'agit", "Est relatif au format de l'outil dont il s'agit (Balado, vid\xe9o, playlist, web s\xe9rie, etc.)"), ('\xc0 propos', '\xc0 propos'), ('Voir et entendre', 'Voir et entendre'), ('Actualit\xe9s, news, nouveaut\xe9', 'Actualit\xe9, news, nouveaut\xe9'), ('Autre', 'Autre')], max_length=200, null=True, verbose_name='Sous quel onglet du site est r\xe9f\xe9renc\xe9 cet outil - Troisi\xe8me onglet \xe0 ouvrir'),
        ),
    ]
