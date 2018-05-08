# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-04 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdmultimedia', '0106_auto_20180503_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='outil',
            name='plus_de_tois_onglet',
            field=models.BooleanField(default=False, verbose_name='S.19. 1 PLUS DE TROIS ONGLETS \xe0 ouvrir pour trouver ce dispositif ?'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='deuxieme_onglet',
            field=models.CharField(choices=[("Ne s'applique pas", "Ne s'applique pas car l'outil \xe9tait disponible sur la page d'accueil"), ("On peut consulter l'outil directement sur cette deuxi\xe8me page", "On peut consulter l'outil directement sur cette deuxi\xe8me page"), ('Action culturelle', 'Action culturelle'), ('M\xe9diation', 'M\xe9diation'), ('\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que', '\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que'), ('Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental', 'Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental'), ('Pour tous les publics', 'Pour tout les publics'), ("L'orchestre et vous", "L'orchestre et vous"), ("Guide d'\xe9coute", "Guide d'\xe9coute"), ('Livret p\xe9dagogique', 'Livret p\xe9dagogique'), ('Pour les enseignants, \xe9coles, scolaires', 'Pour les enseignants, \xe9coles, scolaires'), ('Le nom du dispositif lui m\xeame', "Le nom du dispositif lui m\xeame (ex: 'La galerie symphonique')"), ('Ressources en ligne, ressources num\xe9riques, ressources', 'Ressources en ligne, ressources num\xe9riques, ressources'), ('Relatif \xe0 la programmation', 'Est relatif \xe0 la programmation \xe0 laquelle il fait r\xe9f\xe9rence (onglet du concert, titre du compositeur, etc.)'), ("Relatif au format du dispositif dont il s'agit", "Est relatif au format du dispositif dont il s'agit (Balado, vid\xe9o, playlist, web s\xe9rie, etc.)"), ('\xc0 propos', '\xc0 propos'), ('Voir et entendre', 'Voir et entendre'), ('Actualit\xe9s, news, nouveaut\xe9', 'Actualit\xe9, news, nouveaut\xe9'), ('Pour tous les publics', 'Pour tous les publics'), ('Pour un public sp\xe9cifique', 'Pour un public sp\xe9cifique'), ('Musique', 'Musique'), ('Autre', 'Autre')], default="Ne s'applique pas", max_length=200, null=True, verbose_name='S.18 Quel est le DEUXIEME onglet \xe0 ouvrir pour trouver ce dispositif?'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='premier_onglet',
            field=models.CharField(choices=[("Ne s'applique pas", "Ne s'applique pas"), ("Disponible et consultable sur la page d'acc\xe8s", "L'outil est disponible et consultable sur la page d'acc\xe8s"), ('Action culturelle', 'Action culturelle'), ('M\xe9diation', 'M\xe9diation'), ('\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que', '\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que'), ('Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental', 'Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental'), ('Pour tous les publics', 'Pour tout les publics'), ("L'orchestre et vous", "L'orchestre et vous"), ("Guide d'\xe9coute", "Guide d'\xe9coute"), ('Livret p\xe9dagogique', 'Livret p\xe9dagogique'), ('Pour les enseignants, \xe9coles, scolaires', 'Pour les enseignants, \xe9coles, scolaires'), ('Le nom du dispositif lui m\xeame', "Le nom du dispositif lui m\xeame (ex: 'La galerie symphonique')"), ('Ressources en ligne, ressources num\xe9riques, ressources', 'Ressources en ligne, ressources num\xe9riques, ressources'), ('Relatif \xe0 la programmation', 'Est relatif \xe0 la programmation \xe0 laquelle il fait r\xe9f\xe9rence (onglet du concert, titre du compositeur, etc.)'), ("Relatif au format du dispositif dont il s'agit", "Est relatif au format du dispositif dont il s'agit (Balado, vid\xe9o, playlist, web s\xe9rie, etc.)"), ('\xc0 propos', '\xc0 propos'), ('Voir et entendre', 'Voir et entendre'), ('Actualit\xe9s, news, nouveaut\xe9', 'Actualit\xe9, news, nouveaut\xe9'), ('Pour tous les publics', 'Pour tous les publics'), ('Pour un public sp\xe9cifique', 'Pour un public sp\xe9cifique'), ('Musique', 'Musique'), ('Autre', 'Autre')], default="Ne s'applique pas", max_length=200, null=True, verbose_name='S.17 Quel est le PREMIER onglet \xe0 ouvrir pour trouver ce dispositif?'),
        ),
        migrations.AlterField(
            model_name='outil',
            name='troisieme_onglet',
            field=models.CharField(choices=[('Ne s\u2019applique pas', 'Ne s\u2019applique pas car le dispositif \xe9tait disponible sur la page d\u2019accueil'), ("Ne s'applique pas car l'outil \xe9tait disponible sur la deuxi\xe8me page", "Ne s'applique pas car l'outil \xe9tait disponible sur la deuxi\xe8me page"), ("On peut consulter l'outil directement sur cette troisi\xe8me page", "On peut consulter l'outil directement sur cette trois\xe8me page"), ('Action culturelle', 'Action culturelle'), ('M\xe9diation', 'M\xe9diation'), ('\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que', '\xc9ducation, Apprendre, Le\xe7on, Educoth\xe8que'), ('Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental', 'Exp\xe9rimentation, d\xe9couvrir, exp\xe9rimental'), ('Pour tous les publics', 'Pour tout les publics'), ("L'orchestre et vous", "L'orchestre et vous"), ("Guide d'\xe9coute", "Guide d'\xe9coute"), ('Livret p\xe9dagogique', 'Livret p\xe9dagogique'), ('Pour les enseignants, \xe9coles, scolaires', 'Pour les enseignants, \xe9coles, scolaires'), ('Le nom du dispositif lui m\xeame', "Le nom du dispositif lui m\xeame (ex: 'La galerie symphonique')"), ('Ressources en ligne, ressources num\xe9riques, ressources', 'Ressources en ligne, ressources num\xe9riques, ressources'), ('Relatif \xe0 la programmation', 'Est relatif \xe0 la programmation \xe0 laquelle il fait r\xe9f\xe9rence (onglet du concert, titre du compositeur, etc.)'), ("Relatif au format du dispositif dont il s'agit", "Est relatif au format du dispositif dont il s'agit (Balado, vid\xe9o, playlist, web s\xe9rie, etc.)"), ('\xc0 propos', '\xc0 propos'), ('Voir et entendre', 'Voir et entendre'), ('Actualit\xe9s, news, nouveaut\xe9', 'Actualit\xe9, news, nouveaut\xe9'), ('Pour tous les publics', 'Pour tous les publics'), ('Pour un public sp\xe9cifique', 'Pour un public sp\xe9cifique'), ('Musique', 'Musique'), ('Autre', 'Autre')], default="Ne s'applique pas", max_length=200, null=True, verbose_name='S.19 Quel est le TROISIEME onglet \xe0 ouvrir pour trouver ce dispositif?'),
        ),
    ]
