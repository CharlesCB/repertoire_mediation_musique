# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django_currentuser.db.models import CurrentUserField


OUINON = (
    ("Oui", "Oui"),
    ("Non", "Non"),
)

OUINONNSP = (
    ("Oui", "Oui"),
    ("Non", "Non"),
    ("Nsp","Ne s'applique pas")
)

INTERFACE_LIST = (
    ("Simple consultation", "Simple consultation"),
    ("Participation limitée", "Participation limitée (l'usager est actif mais se contente de répondre aux consignes)"),
    ("Participation dynamique", "Participation dynamique (l'usager co-construit le service)"),
)

PERSONNIFICATION_LIST = (
    ("Service générique", "Service générique"),
    ("Service spécialisé", "Service spécialisé (public catégorisé)"),
    ("Service personnalisé et/ou individualisé", "Service personnalisé et/ou individualisé"),
)

PREM_ONGLET_LIST = (
    ("Ne s'applique pas", "Ne s'applique pas"),
    ("Disponible et consultable sur la page d'accès", "L'outil est disponible et consultable sur la page d'accès"),
    ("Action culturelle", "Action culturelle"),
    ("Médiation", "Médiation"),
    ("Éducation, Apprendre, Leçon, Educothèque", "Éducation, Apprendre, Leçon, Educothèque"),
    ("Expérimentation, découvrir, expérimental", "Expérimentation, découvrir, expérimental"),
    ("Pour tous les publics", "Pour tout les publics"),
    ("L'orchestre et vous", "L'orchestre et vous"),
    ("Guide d'écoute", "Guide d'écoute"),
    ("Livret pédagogique", "Livret pédagogique"),
    ("Pour les enseignants, écoles, scolaires", "Pour les enseignants, écoles, scolaires"),
    ("Le nom du dispositif lui même", "Le nom du dispositif lui même (ex: 'La galerie symphonique')"),
    (
    "Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format du dispositif dont il s'agit",
     "Est relatif au format du dispositif dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
    ("Pour tous les publics","Pour tous les publics"),
    ("Pour un public spécifique","Pour un public spécifique"),
    ("Musique","Musique"),
    ("Autre", "Autre")
)

DEUX_ONGLET_LIST = (
    ("Ne s'applique pas", "Ne s'applique pas car l'outil était disponible sur la page d'accueil"),
    ("On peut consulter l'outil directement sur cette deuxième page",
     "On peut consulter l'outil directement sur cette deuxième page"),
    ("Action culturelle", "Action culturelle"),
    ("Médiation", "Médiation"),
    ("Éducation, Apprendre, Leçon, Educothèque", "Éducation, Apprendre, Leçon, Educothèque"),
    ("Expérimentation, découvrir, expérimental", "Expérimentation, découvrir, expérimental"),
    ("Pour tous les publics", "Pour tout les publics"),
    ("L'orchestre et vous", "L'orchestre et vous"),
    ("Guide d'écoute", "Guide d'écoute"),
    ("Livret pédagogique", "Livret pédagogique"),
    ("Pour les enseignants, écoles, scolaires", "Pour les enseignants, écoles, scolaires"),
    ("Le nom du dispositif lui même", "Le nom du dispositif lui même (ex: 'La galerie symphonique')"),
    (
    "Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format du dispositif dont il s'agit",
     "Est relatif au format du dispositif dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
    ("Pour tous les publics", "Pour tous les publics"),
    ("Pour un public spécifique", "Pour un public spécifique"),
    ("Musique", "Musique"),
    ("Autre", "Autre")
)

TROIS_ONGLET_LIST = (
    ("Ne s’applique pas","Ne s’applique pas car le dispositif était disponible sur la page d’accueil"),
    ("Ne s'applique pas car l'outil était disponible sur la deuxième page", "Ne s'applique pas car l'outil était disponible sur la deuxième page"),
    ("On peut consulter l'outil directement sur cette troisième page",
     "On peut consulter l'outil directement sur cette troisème page"),
    ("Action culturelle", "Action culturelle"),
    ("Médiation", "Médiation"),
    ("Éducation, Apprendre, Leçon, Educothèque", "Éducation, Apprendre, Leçon, Educothèque"),
    ("Expérimentation, découvrir, expérimental", "Expérimentation, découvrir, expérimental"),
    ("Pour tous les publics", "Pour tout les publics"),
    ("L'orchestre et vous", "L'orchestre et vous"),
    ("Guide d'écoute", "Guide d'écoute"),
    ("Livret pédagogique", "Livret pédagogique"),
    ("Pour les enseignants, écoles, scolaires", "Pour les enseignants, écoles, scolaires"),
    ("Le nom du dispositif lui même", "Le nom du dispositif lui même (ex: 'La galerie symphonique')"),
    (
    "Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format du dispositif dont il s'agit",
     "Est relatif au format du dispositif dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
    ("Pour tous les publics", "Pour tous les publics"),
    ("Pour un public spécifique", "Pour un public spécifique"),
    ("Musique", "Musique"),
    ("Autre", "Autre")
)

EPOQUE_LIST = (
    ("Avant le XIIè", "Avant le XIIè"),
    ("XIIè", "XIIè"),
    ("XIIIè", "XIIIè"),
    ("XIVè", "XIVè"),
    ("XVè", "XVè"),
    ("XVIè", "XVIè"),
    ("XVIIè", "XVIIè"),
    ("XVIIIè", "XVIIIè"),
    ("XIXè", "XIXè"),
    ("XXè", "XXè"),
    ("XXIè", "XXIè"),
    ("nsp","nsp")
)

ACCESSIBILITE_LIST = (
    ("Oui", "Oui"),
    ("Non", "Non"),
    ("Ne s'applique pas", "Ne s'applique pas")
)

SONORE_VALEUR_LIST = (
    ("Nsp", "Ne s'applique pas"),
    ("Premier plan", "Premier Plan"),
    ("Arrière plan", "Arrière plan"),
    ("Alternance", "Alternance")
)

EVOCATION_LITTERAIRE_LIST = (
    ("Non", "Non"),
    ("Texte oral", "Texte oral"),
    ("Texte écrit", "Texte écrit")
)

@python_2_unicode_compatible
class ProdType(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "types de producteur"


@python_2_unicode_compatible
class ProducteurNom(models.Model):
    nom = models.CharField(max_length=200, unique = True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Nom du producteur"


@python_2_unicode_compatible
class SupportDiffusion(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "supports de diffusion"


@python_2_unicode_compatible
class FormeNarrative(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "forme narrative"


@python_2_unicode_compatible
class ModeHebergement(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Mode d'hébergement sur la toile"


@python_2_unicode_compatible
class ModeConsultation(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Mode de consultation offert au public"


@python_2_unicode_compatible
class LangueNarration(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Langue de la narration"


@python_2_unicode_compatible
class SousTitre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Sous-titre"


@python_2_unicode_compatible
class Orchestration(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Sons et orchestration"


@python_2_unicode_compatible
class Structure(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Structures"


@python_2_unicode_compatible
class LanguageMusical(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Languages musical"


@python_2_unicode_compatible
class GenreMusical(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Genres musical"


@python_2_unicode_compatible
class StyleMusical(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Styles musical"


@python_2_unicode_compatible
class ExperienceMusicale(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Experiences musical"


@python_2_unicode_compatible
class Contexte(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Contexte de composition, création, interprétation..."


@python_2_unicode_compatible
class RoleEvolution(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Rôle et évolution"


@python_2_unicode_compatible
class SollicitationMusicale(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Sollicitation musicale"


@python_2_unicode_compatible
class SollicitationGenerale(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Sollicitation générale"


@python_2_unicode_compatible
class EvocationGraphique(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Évocations graphique"


@python_2_unicode_compatible
class EvocationPlastique(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Évocations plastique"


@python_2_unicode_compatible
class EvocationAutre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Évocations d'autre discipline"


@python_2_unicode_compatible
class RoleHomme(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des homme"


@python_2_unicode_compatible
class RoleFemmes(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des femme"


@python_2_unicode_compatible
class RoleHumainNeutre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des humain indéterminé"


@python_2_unicode_compatible
class RolePersAnimHomme(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des personnages animés homme"


@python_2_unicode_compatible
class RolePersAnimFemmes(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des personnages animés femme"


@python_2_unicode_compatible
class RolePersAnimNeutre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des personnages animés indéterminé"


@python_2_unicode_compatible
class RoleAnimauxHomme(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des male"


@python_2_unicode_compatible
class RoleAnimauxFemmes(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des femelle"


@python_2_unicode_compatible
class RoleAnimauxNeutre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des animaux indéterminé"


@python_2_unicode_compatible
class RoleInstrHomme(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des instruments homme"


@python_2_unicode_compatible
class RoleInstrFemmes(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des instruments femme"


@python_2_unicode_compatible
class RoleInstrNeutre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Role des instruments indéterminé"


@python_2_unicode_compatible
class FormatOutil(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "format du dispositif"


@python_2_unicode_compatible
class NotionsInter(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "exemples de notions évoquées de façon interdisciplinaires"



@python_2_unicode_compatible
class Outil(models.Model):
    titre = models.CharField(max_length=200, verbose_name="R.1 Titre du dispositif")
    page_outil = models.BooleanField(default = False, verbose_name = "Afficher directement une page qui fait office de dispositif")
    integration = models.TextField(blank = True, verbose_name = "code pour l'integration du dispositif (si applicable)")
    url = models.CharField(unique=True, max_length=200, verbose_name="R.2 URL d'accès direct",
                           help_text="Attention, enlever la barre oblique « / » à la fin de l’URL Ex. www.osm.ca/fr/matinees/#1488205065259-011decba-7105")
    site = models.URLField(max_length=200, verbose_name="R.3 URL d'accès au site d'hébergement", blank=False,
                           help_text="Attention, enlever la barre oblique « / » à la fin de l’URL www.osm.ca. <br> Si le dispositif est une vidéo d’un-e YouTubeur-e, indiquer le lien vers sa chaîne YouTube.")
    ensemble_thematique = models.CharField(blank=False, choices=OUINON, max_length=4, default="Non",
                                           verbose_name="R.3.1 Ce dispositif fait-il partie d'un ensemble thématique du même type? (regroupé par l'organisme producteur)",
                                           help_text = "On parle bien ici d’un ensemble thématique et non pas d’un regroupement par format (ex. vidéo) ou par objectif (ex . ressource pédagogique). ")
    ensemble_thematique_nom = models.CharField(max_length=200, verbose_name="R.3.2 Si oui, donnez le titre sous lequel est regroupé cet ensemble.",
                                               blank=True, help_text="Ex: Camille raconte")
    producteur_type = models.ManyToManyField(ProdType, verbose_name="R.4 Qui est le producteur de ce dispositif?",
                                             help_text = "Attention : répondre à cette question nécessite d’aller vérifier les statuts des organismes impliqués ou le titre auquel ils s’impliquent. Exemple . L’OSM peut agir en tant que producteur pour un concert ou au titre de diffuseur pour un autre évènement.")
    #producteur_nom = models.ManyToManyField(ProducteurNom, verbose_name="R.5 Préciser le nom complet du/des producteur(s)")
    producteur_nom = models.CharField(max_length=200, verbose_name="R.5 Préciser le nom complet du/des producteur(s)", blank = True)
    support_diffusion = models.ManyToManyField(SupportDiffusion, verbose_name="R.6 Support de diffusion")
    format = models.ManyToManyField(FormatOutil, verbose_name="R.7 Format du dispositif")
    forme_narrative = models.ManyToManyField(FormeNarrative, verbose_name="R.8 Formes narratives")
    duree = models.CharField(max_length=8, null=False, verbose_name="R.9 Durée", default="00:00:00",
                             help_text="nsp = ne s'applique pas, ddv = durée d’écoute variable. La durée d’écoute est variable puisque les utilisateurs peuvent décider, ou non, de regarder les vidéos. Concerne les dispositifs qui allient texte et vidéo.")
    nb_pages = models.PositiveIntegerField(null=True, verbose_name="R.10 Nombre de pages", default=0,
                                           help_text="Correspond au nombre de page web sur lesquelles se décline le  dispositif .")
    mise_en_ligne_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                          verbose_name="R.11 Date de la mise en ligne",
                                          help_text="Si seule l’année de mise en ligne est disponible entrer la date de mise en ligne au 1er janvier de l’année concernée")
    depouillement_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                          verbose_name="R.12 Date du dépouillement")
    interface = models.CharField(choices=INTERFACE_LIST,
                                 max_length=200,
                                 null=True,
                                 verbose_name="R.13 Que permet l'interface?")
    materiel_imprimer = models.CharField(choices=OUINON, max_length = 200, default = "Non",
                                         verbose_name = "R.13.1 Le dispositif comprend-il du matériel à imprimer (ex. livret en pdf) ?")
    personnification_service = models.CharField(null=True, max_length=200, choices=PERSONNIFICATION_LIST,
                                                verbose_name="R.14 Degrés de personnification du service")
    commentaire_possible = models.BooleanField(verbose_name="R.15 Possibilité de laisser des commentaires",
                                               help_text="Compter les commentaires qui apparaissent sur la page de consultation du dispositif (ex. Si il n’y a pas de possibilité de commentaire sur les capsules de l’OSM mais que les commentaires sont possibles sur l’hébergement youtube ne pas cocher)")
    commentaire_nombre = models.PositiveIntegerField(null=True, blank=True, verbose_name="R.16 Nombre de commentaires")
    premier_onglet = models.CharField(choices=PREM_ONGLET_LIST,
                                      max_length=200,
                                      default="Ne s'applique pas",
                                      null=True,
                                      verbose_name="S.17 Quel est le PREMIER onglet à ouvrir pour trouver ce dispositif?")
    prem_onglet_autre = models.CharField(blank=True, null=True, max_length=200, verbose_name="Si autre, précisez")
    deuxieme_onglet = models.CharField(choices=DEUX_ONGLET_LIST,
                                       max_length=200,
                                       default="Ne s'applique pas",
                                       null=True,
                                       verbose_name="S.18 Quel est le DEUXIEME onglet à ouvrir pour trouver ce dispositif?")
    deux_onglet_autre = models.CharField(blank=True, null=True, max_length=200, verbose_name="Si autre, précisez")
    troisieme_onglet = models.CharField(choices=TROIS_ONGLET_LIST,
                                        max_length=200,
                                        default="Ne s'applique pas",
                                        null=True,
                                        verbose_name="S.19 Quel est le TROISIEME onglet à ouvrir pour trouver ce dispositif?")
    trois_onglet_autre = models.CharField(blank=True, null=True, max_length=200, verbose_name="Si autre, précisez")
    plus_de_tois_onglet = models.BooleanField(verbose_name = "S.19. 1 PLUS DE TROIS ONGLETS à ouvrir pour trouver ce dispositif ?", default = False)

    mode_hebergement = models.ManyToManyField(ModeHebergement, verbose_name="S.20 Mode d'hébergement sur la toile")
    mode_consultation = models.ManyToManyField(ModeConsultation, verbose_name="S.21 Mode de consultation offert au public")
    narration_langue = models.ManyToManyField(LangueNarration, verbose_name="S.22 Langue du dispositif")
    sous_titre = models.ManyToManyField(SousTitre, verbose_name="S.23 Sous-titrage",
                                        help_text="Les sous-titrages automatiques proposés par YouTube n’entrent pas en considération.")

    ##Accessibilité
    malentendants = models.CharField(choices=OUINON,
                                     max_length=200,
                                     null=False,
                                     default="Non",
                                     verbose_name="S.24.1 Ce dispositif est-il intégralement accessible aux malentendants (Sous titrage, language des signes)")
    malvoyants = models.CharField(choices=OUINON,
                                  max_length=200,
                                  null=False,
                                  default="Non",
                                  verbose_name="S.24.2 Ce dispositif est-il intégralement accessible aux malvoyants (audiodescription)")
    ## Quid du materiau musical
    materiau_musical = models.CharField(choices=OUINON,
                                        max_length=200,
                                        default="Non",
                                        verbose_name="M.25 Parle-t-on du matériau musical?",
                                        help_text = 'Registres (au sens de groupe de hauteur si cela concerne les registres de l’orgue cocher « timbres »)')
    orchestration = models.ManyToManyField(Orchestration,
                                           verbose_name="M.25.1 Parle-t-on du son et de l'orchestration, si oui précisez.")
    structure = models.ManyToManyField(Structure, verbose_name="M.25.2 Parle-t-on de la structure, si oui précisez.")
    language_musical = models.ManyToManyField(LanguageMusical,
                                              verbose_name="M.25.3 Parle-t-on du language musical, si oui précisez.")
    genre_musical = models.ManyToManyField(GenreMusical, verbose_name="M.25.4 Parle-t-on du genre musical, si oui précisez.")
    style_musical = models.ManyToManyField(StyleMusical, verbose_name="M.25.5 Parle-t-on du style musical, si oui précisez.")
    ## Quid de
    experience_musicale = models.ManyToManyField(ExperienceMusicale,
                                                 verbose_name="M.26 Parle-t-on de l'experience musicale, si oui précisez.")
    elements_socioculturels = models.CharField(choices=OUINON,
                                               max_length=200,
                                               default="Non",
                                               verbose_name="M.27 Parle-t-on des éléments socioculturels et historiques?")
    epoque = MultiSelectField(choices=EPOQUE_LIST,
                              null=True,
                              max_length=50,
                              verbose_name="M.27.1 Époque")
    contexte = models.ManyToManyField(Contexte,
                                      verbose_name="M.27.2 Parle-t-on du contexte de composition, création, interprétation de l'oeuvre, de l'instrument...",
                                      help_text='Si il est juste fait mention d’une date sans donner plus d’information sur ce qui se passait à l’époque cocher “Non”.')
    role_evolution = models.ManyToManyField(RoleEvolution, verbose_name="M.27.3 Parle-t-on du rôle et de l'évolution du")
    sollicitation_musicale = models.ManyToManyField(SollicitationMusicale,
                                                    verbose_name="U.28 Comment sollicite-t-on musicalement l'usager?")
    sollicitation_generale = models.ManyToManyField(SollicitationGenerale,
                                                    verbose_name="U.29 En général (hors musique) comment sollicite-t-on l'usager?")

    # Usages du sonore
    temps_mus = models.CharField(max_length=8, null=False, verbose_name="PM.30 Temps de musique seule (hh:mm:ss)",
                                 default="00:00:00", help_text="nsp = ne s'applique pas")
    temps_par = models.CharField(max_length=8, null=False, verbose_name="PM.31 Temps de parole seule (hh:mm:ss)",
                                 default="00:00:00", help_text="nsp = ne s'applique pas")
    temps_mus_par = models.CharField(max_length=8, null=False,
                                     verbose_name="PM.32 Temps de parole et musique superposées (hh:mm:ss)",
                                     default="00:00:00", help_text="nsp = ne s'applique pas")
    sonore_valeur = models.CharField(choices=SONORE_VALEUR_LIST,
                                     max_length=200,
                                     null=False,
                                     default="Nsp",
                                     verbose_name="PM.33 Mise en valeur du sonore")
    # Outre les sons, comment évoque-t-on le matériau musical?
    evocation_graphique = models.ManyToManyField(EvocationGraphique,
                                           verbose_name="EM.34 Évocation graphique")
    evocation_plastique = models.ManyToManyField(EvocationPlastique,
                                           verbose_name="EM.35 Évocation plastique")
    evocation_litteraire = MultiSelectField(choices=EVOCATION_LITTERAIRE_LIST,
                                            max_length=200,
                                            null=False,
                                            verbose_name="EM.36 Évocation littéraire")
    evocation_autre = models.ManyToManyField(EvocationAutre,
                                       verbose_name="I.37 Autres disciplines évoquées")

    # à partir de quelle notion?
    notion_concepts = models.CharField(choices = OUINONNSP,
                                       max_length = 50,
                                       null = False,
                                       default = "Nsp",
                                       verbose_name="I.38 À partir de quelle notion? - Notions communes (luminosité, transparence, vitesse, mouvement)")
    notion_experiences = models.CharField(choices = OUINONNSP,
                                       max_length = 50,
                                       null = False,
                                       default = "Nsp",
                                       verbose_name="I.38 À partir de quelle notion? - Expérience (émotions)")
    notion_pratiques = models.CharField(choices = OUINONNSP,
                                       max_length = 50,
                                       null = False,
                                       default = "Nsp",
                                       verbose_name="I.38 À partir de quelle notion? - Pratique (processus de création)")
    exemples_notions_interdisciplinaires = models.ManyToManyField(NotionsInter,
                                                                  blank = True,
                                                                  verbose_name="I.39 Donner des exemples de notions évoquées de façon interdisciplinaires")

    # stéréotypes et clichés
    humain = models.CharField(choices = OUINON,
                              max_length = 50,
                              null = False,
                              default = "Non",
                              verbose_name = "Sté.39 Y-a-t-il des humains? (compter les personnes qui ont un rôle dans la narration, qui sont maximum 3 dans le champ ou plein cadre)")
    nb_humains_total = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre d'humains total", default=0)
    nb_hommes = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre d'hommes", default=0)
    nb_femmes = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre de femmes", default=0)
    nb_humains_indetermines = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre d'humains au genre indéterminé",
                                                          default=0)
    role_humain_femme = models.ManyToManyField(RoleFemmes,
                                               verbose_name="Sté.39.2 Rôle des femmes")
    role_humain_homme = models.ManyToManyField(RoleHomme,
                                                verbose_name="Sté.39.3 Rôle des hommes")
    role_humain_neutre = models.ManyToManyField(RoleHumainNeutre,
                                                verbose_name="Sté.39.4 Rôle des indeterminés")
    pers_anime = models.CharField(choices=OUINON,
                              max_length=50,
                              null=False,
                              default="Non",
                              verbose_name="Sté.40 Y-a-t-il des personnages animés?")
    nb_pers_anime_total = models.PositiveIntegerField(null=True, verbose_name="Sté.40.1 Nombre de personnages animés total",
                                                      default=0)
    nb_pers_anime_hommes = models.PositiveIntegerField(null=True, verbose_name="Sté.40.1 Nombre de personnages animés hommes",
                                                       default=0)
    nb_pers_anime_femmes = models.PositiveIntegerField(null=True, verbose_name="Sté.40.1 Nombre de personnages animés femmes",
                                                       default=0)
    nb_pers_anime_indetermines = models.PositiveIntegerField(null=True,
                                                             verbose_name="Sté.40.1 Nombre de personnages animés au genre indéterminé",
                                                             default=0)
    role_pers_anime_femme = models.ManyToManyField(RolePersAnimFemmes,
                                                   verbose_name="Sté.40.3 Rôle des personnages animés féminins")
    role_pers_anime_homme = models.ManyToManyField(RolePersAnimHomme,
                                                   verbose_name="Sté.40.2 Rôle des personnages animés masculins")
    role_pers_anime_neutre = models.ManyToManyField(RolePersAnimNeutre,
                                                    verbose_name="Sté.40.4 Rôle des personnages animés indéterminés")
    animaux = models.CharField(choices=OUINON,
                              max_length=50,
                              null=False,
                              default="Non",
                              verbose_name="Sté.41 Y-a-t-il des animaux?")
    nb_animaux_total = models.PositiveIntegerField(null=True, verbose_name="Sté.41.1 Nombre d'animaux total", default=0)
    nb_males = models.PositiveIntegerField(null=True, verbose_name="Sté.41.1 Nombre de mâles", default=0)
    nb_femelles = models.PositiveIntegerField(null=True, verbose_name="Sté.41.1 Nombre de femelles", default=0)
    nb_animaux_indetermines = models.PositiveIntegerField(null=True,
                                                          verbose_name="Sté.41.1 Nombre d'animaux au genre indéterminé",
                                                          default=0)
    role_animaux_femme = models.ManyToManyField(RoleAnimauxFemmes,
                                                verbose_name="Sté.41.3 Rôle des animaux femelles")
    role_animaux_homme = models.ManyToManyField(RoleAnimauxHomme,
                                                verbose_name="Sté.41.2 Rôle des animaux mâles")
    role_animaux_neutre = models.ManyToManyField(RoleAnimauxNeutre,
                                                 verbose_name="Sté.41.4 Rôle des animaux indéterminés")
    instr_anime = models.CharField(choices=OUINON,
                              max_length=50,
                              null=False,
                              default="Non",
                              verbose_name="Sté.42 Y-a-t-il des instruments animés")
    nb_instr_anime_total = models.PositiveIntegerField(null=True, verbose_name="Sté.42.1 Nombre d'instruments animés total",
                                                       default=0)
    nb_instr_anime_hommes = models.PositiveIntegerField(null=True, verbose_name="Sté.42.1 Nombre d'instruments animés masculins",
                                                        default=0)
    nb_instr_anime_femmes = models.PositiveIntegerField(null=True, verbose_name="Sté.42.1 Nombre d'instruments animés féminins",
                                                        default=0)
    nb_instr_anime_indetermines = models.PositiveIntegerField(null=True,
                                                              verbose_name="Sté.42.1 Nombre d'instruments animés au genre indéterminé",
                                                              default=0)
    role_instr_anime_femme = models.ManyToManyField(RoleInstrFemmes,
                                                    verbose_name="Sté.42.3 Rôle des instruments anthropomorphes féminins")
    role_instr_anime_homme = models.ManyToManyField(RoleInstrHomme,
                                                    verbose_name="Sté.42.2 Rôle des instruments anthropomorphes masculins")
    role_instr_anime_neutre = models.ManyToManyField(RoleInstrNeutre,
                                                     verbose_name="Sté.42.4 Rôle des instruments anthropomorphes neutres")

    utilisateur = CurrentUserField()

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.titre
