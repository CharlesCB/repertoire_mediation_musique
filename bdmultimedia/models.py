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

PRODUCTEUR_TYPE_LIST = (
    ("Particulier", "Particulier"),
    ("Organisme de diffusion (OSM; Festival)", "Organisme de diffusion (OSM; Festival)"),
    ("Organisme de formation professionnelle (CQM; ARIAM; CFMI)",
     "Organisme de formation professionnelle (CQM; ARIAM; CFMI)"),
    ("Groupe de recherche (P2M; Groupe de recherche sur la médiation culturelle)",
     "Groupe de recherche (P2M; Groupe de recherche sur la médiation culturelle)"),
    ("Organismes éducatif (Ecole de musique; TEDX)", "Organismes éducatif (Ecole de musique; TEDX)"),
    ("Autre", "Autre"),
)

SUPPORT_DIFFUSION_LIST = (
    ("Ordinateur", "Ordinateur"),
    ("Smartphone", "Smartphone"),
    ("Tablette", "Tablette"),
    ("Lunettes 3D", "Lunettes 3D"),
    ("Consoles de JV", "Consoles de JV"),
    ("DVD", "DVD"),
    ("CD", "CD"),
    ("Autre", "Autre"),
)
FORMAT_LIST = (
    ("Ecrit (texte; dessin)", "Ecrit (texte; dessin)"),
    ("Audio", "Audio"),
    ("Audiovisuel", "Audiovisuel"),
    ("Immersif", "Immersif"),
    ("Réalité augmentée", "Réalité augmentée"),
    ("Autre", "Autre"),
)
FORME_NARRATIVE_LIST = (
    ("Entrevue", "Entrevue"),
    ("Fiction", "Fiction"),
    (
        "Synopsis (récit fidèle au programme de l'oeuvre)",
        "Synopsis (récit fidèle au programme de l'oeuvre)",
    ),
    (
        "Web-série (plusieurs occurences qui ont un lien entre elles)",
        "Web-série (plusieurs occurences qui ont un lien entre elles)",
    ),
    ("Animation", "Animation"),
    ("Art et essai", "Art et essai"),
    ("Vulgarisation", "Vulgarisation"),
    ("Creative commons (sur le modèle wiki)", "Creative commons (sur le modèle wiki)"),
    ("Reportage", "Reportage"),
    ("Jeu", "Jeu"),
    ("Autre", "Autre"),
)

INTERFACE_LIST = (
    ("Simple consultation", "Simple consultation"),
    ("Participation limitée", "Participation limitée (l'usager est actif mais se contente de répondre aux consignes)"),
    ("Participation dynamique", "Participation dynamique (l'usager co-construit le service)"),
    ("Autre", "Autre"),
)

PERSONNIFICATION_LIST = (
    ("Service générique", "Service générique"),
    ("Service spécialisé", "Service spécialisé (public catégorisé)"),
    ("Service personnalisé et/ou individualisé", "Service personnalisé et/ou individualisé"),
    ("Autre", "Autre"),
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
    ("Le nom de l'outil lui même", "Le nom de l'outil lui même (ex: 'La galerie symphonique')"),
    (
    "Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format de l'outil dont il s'agit",
     "Est relatif au format de l'outil dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
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
    ("Le nom de l'outil lui même", "Le nom de l'outil lui même (ex: 'La galerie symphonique')"),
    (
    "Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format de l'outil dont il s'agit",
     "Est relatif au format de l'outil dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
    ("Autre", "Autre")
)

TROIS_ONGLET_LIST = (
    ("Ne s'applique pas", "Ne s'applique pas car l'outil était disponible sur la deuxième page"),
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
    ("Le nom de l'outil lui même", "Le nom de l'outil lui même (ex: 'La galerie symphonique')"),
    (
    "Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format de l'outil dont il s'agit",
     "Est relatif au format de l'outil dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
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
    ("XXIè", "XXIè")
)

NARRATION_LANGUE_LIST = (
    ("Français", "Français"),
    ("Anglais", "Anglais"),
    ("Espagnol", "Espagnol"),
    ("Allemand", "Allemand"),
    ("Italien", "Italien"),
    ("Portugais", "Portugais"),
    ("Autre", "Autre"),
)

SOUS_TITRE_LIST = (
    ("Pas de sous titrage", "Pas de sous titrage"),
    ("Français", "Français"),
    ("Anglais", "Anglais"),
    ("Espagnol", "Espagnol"),
    ("Allemand", "Allemand"),
    ("Italien", "Italien"),
    ("Portugais", "Portugais"),
    ("Autre", "Autre"),
)

ACCESSIBILITE_LIST = (
    ("Oui", "Oui"),
    ("Non", "Non"),
    ("Ne s'applique pas", "Ne s'applique pas")
)

MATERIAU_MUSICAL_LIST = (
    ("Non", "Non"),
    ("Son", "Son"),
    ("Structure", "Structure"),
    ("Language musical", "Language musical"),
    ("Genre (opéra; symphonique)", "Genre (opéra; symphonique)"),
    ("Style (Classique; Romantique; Contemporain)", "Style (Classique; Romantique; Contemporain)"),
    ("Autre", "Autre"),
)
PRATIQUE_MUSICALE_LIST = (
    (
        "Non",
        "Non"
    ),
    (
        "Techniques instrumentales (mode de production du son)",
        "Techniques instrumentales (mode de production du son)"
    ),
    (
        "Activité du musicien; du compositeur; de l'interprète; du luthier etc.",
        "Activité du musicien; du compositeur; de l'interprète; du luthier etc."
    ),
    (
        "Pratique professionnelle",
        "Pratique professionnelle"
    ),
    (
        "Pratique amateur",
        "Pratique amateur"
    ),
    (
        "Autre",
        "Autre"
    ),
)
EXPERIENCES_LIST = (
    (
        "Non",
        "Non"
    ),
    (
        "Techniques d'écoute",
        "Techniques d'écoute"
    ),
    (
        "Expérience vécue",
        "Expérience vécue"
    ),
    (
        "Le concert",
        "Le concert"
    ),
    (
        "Les répétitions (générale; raccord; etc.)",
        "Les répétitions (générale; raccord; etc.)"
    ),
    (
        "Autre",
        "Autre"
    ),
)

ELEMENTS_SOCIO_LIST = (
    ("Non", "Non"),
    ("Vie du compositeur; interprète; dédicaçaire; mécène",
     "Vie du compositeur; interprète; dédicaçaire; mécène"),
    ("Organologie", "Organologie"),
    ("Lutherie", "Lutherie"),
    ("Évolution de la profession",
     "Évolution de la profession"),
    ("Conventions", "Conventions"),
    ("Epoques datées (ex. les dates du Romantisme ou référence au 18è)",
     "Epoques datées (ex. les dates du Romantisme ou référence au 18è)"),
    ("Oeuvres (à titre documentaires)", "Oeuvres (à titre documentaires)"),
    ("Contexte de production", "Contexte de production"),
    ("Contexte de réception", "Contexte de réception"),
    ('Contexte de création (au sens de "la première")',
     'Contexte de création (au sens de "la première")'),
    ("Autre", "Autre")
)

SOLICITATION_MUSICALE_LIST = (
    ("Interpréter", "Interpréter"),
    ("Reproduire", "Reproduire"),
    ("Écouter", "Écouter"),
    ("Inventer/composer/improviser", "Inventer/composer/improviser"),
    ("Lire", "Lire"),
    ("Regarder", "Regarder"),
    ("Autre", "Autre")
)

SOLICITATION_AUTRE_LIST = (
    ("Lire", "Lire"),
    ("Regarder", "Regarder"),
    ("Bricoler", "Bricoler"),
    ("Jouer (au sens ludique)", "Jouer (au sens ludique)"),
    ("Écrire", "Écrire"),
    ("Autre", "Autre")
)

SONORE_VALEUR_LIST = (
    ("Nsp", "Ne s'applique pas"),
    ("Premier plan", "Premier Plan"),
    ("Arrière plan", "Arrière plan"),
    ("Alternance", "Alternance")
)

EVOCATION_GRAPHIQUE_LIST = (
    ("Non", "Non"),
    ("Représentation graphique traditionnelle (partition + notes)",
     "Représentation graphique traditionnelle (partition + notes)"),
    ("Représentation graphique traditionnelle augmentée (Ex. les notes s'éclairent quand on les entends)",
     "Représentation graphique traditionnelle augmentée (Ex. les notes s'éclairent quand on les entends)"),
    (
    "Représentation graphique traditionelle illustrée (Ex. les notes sont en fait des oiseaux sur les lignes de la portée)",
    "Représentation graphique traditionelle illustrée (Ex. les notes sont en fait des oiseaux sur les lignes de la portée)"),
    (
    "Représentation graphique schématisée (Ex. il y toujours un portée mais ce sont des courbes qui figurent la mélodie)",
    "Représentation graphique schématisée (Ex. il y toujours un portée mais ce sont des courbes qui figurent la mélodie)"),
    ("Représentation graphique symbolisée (Ex. des images animées; cf. ratatouille!!)",
     "Représentation graphique symbolisée (Ex. des images animées; cf. ratatouille!!)"),
    ("Autre", "Autre")
)

EVOCATION_PLASTIQUE_LIST = (
    ("Non", "Non"),
    ("Sculpture", "Sculpture"),
    ("Installation", "Installation"),
    ("Autre", "Autre")
)

EVOCATION_LITTERAIRE_LIST = (
    ("Non", "Non"),
    ("Texte oral", "Texte oral"),
    ("Texte écrit", "Texte écrit")
)

EVOCATION_AUTRE_LIST = (
    ("Aucune", "Aucune"),
    ("Littérature", "Littérature"),
    ("Danse", "Danse"),
    ("Art plastiques", "Art plastiques"),
    ("Théâtre", "Théâtre"),
    ("Cinéma", "Cinéma"),
    ("Arts numériques", "Arts numériques"),
    ("Sports", "Sports"),
    ("Neurosciences", "Neurosciences"),
    ("Sciences physiques", "Sciences physiques"),
    ("Architechture", "Architechture"),
    ("Gastronomie", "Gastronomie"),
    ("Cirque", "Cirque"),
    ("Performance", "Performance"),
    ("Anatomie", "Anatomie"),
    ("Autre", "Autre")
)


@python_2_unicode_compatible
class ProdType(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "types de producteur"


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
        verbose_name = "format de l'outil"


@python_2_unicode_compatible
class NotionsInter(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "exemples de notions évoquées de façon interdisciplinaires"



@python_2_unicode_compatible
class Outil(models.Model):
    titre = models.CharField(max_length=200, verbose_name="R.1 Titre de l'outil")
    integration = models.TextField(blank = True, verbose_name = "code pour l'integration de l'outil (si applicable)")
    url = models.CharField(unique=True, max_length=200, verbose_name="R.2 Chemin d'accès direct",
                           help_text="Dernier URL à suivre pour ateindre l'outil - nsp = ne s'applique pas")
    site = models.URLField(max_length=200, verbose_name="R.3 Chemin d'accès au site d'hébergement", blank=False,
                           help_text="ex. site de la Philharmonie de Paris")
    ensemble_thematique = models.CharField(blank=False, choices=OUINON, max_length=4, default="Non",
                                           verbose_name="R.3.1 Cet outil fait-il partie d'un ensemble thématique du même type? (regroupé par l'organisme producteur)")
    ensemble_thematique_nom = models.CharField(max_length=200, verbose_name="R.3.2 Si oui, quel est le nom de cet ensemble?",
                                               blank=True)
    producteur_type = models.ManyToManyField(ProdType, verbose_name="R.4 Qui est le producteur de cet outil?")
    producteur_nom = models.CharField(max_length=200, verbose_name="R.5 Préciser le nom complet du/des producteur(s)")
    support_diffusion = models.ManyToManyField(SupportDiffusion, verbose_name="R.6 Support de diffusion")
    format = models.ManyToManyField(FormatOutil, verbose_name="R.7 Format de l'outil")
    forme_narrative = models.ManyToManyField(FormeNarrative, verbose_name="R.8 Forme narrative générale")
    duree = models.CharField(max_length=8, null=False, verbose_name="R.9 Durée", default="00:00:00",
                             help_text="nsp = ne s'applique pas")
    nb_pages = models.PositiveIntegerField(null=True, verbose_name="R.10 Nombre de pages", default=0)
    mise_en_ligne_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                          verbose_name="R.11 Date de la mise en ligne",
                                          help_text="laisser vide si non disponible")
    depouillement_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                          verbose_name="R.12 Date du dépouillement")
    interface = models.CharField(choices=INTERFACE_LIST,
                                 max_length=200,
                                 null=True,
                                 verbose_name="R.13 Que permet l'interface?")
    interface_autre = models.CharField(null=True, blank=True, max_length=400, verbose_name="Si autre, précisez")
    personnification_service = models.CharField(null=True, max_length=200, choices=PERSONNIFICATION_LIST,
                                                verbose_name="R.14 Degrés de personnification du service")
    personnification_autre = models.CharField(null=True, blank=True, max_length=400, verbose_name="Si autre, précisez")
    commentaire_possible = models.BooleanField(verbose_name="R.15 Possibilité de laisser des commentaires")
    commentaire_nombre = models.PositiveIntegerField(null=True, blank=True, verbose_name="R.16 Nombre de commentaires",
                                                     help_text="Laisser vide si les commentaires sont impossibles")
    premier_onglet = models.CharField(choices=PREM_ONGLET_LIST,
                                      max_length=200,
                                      default="Ne s'applique pas",
                                      null=True,
                                      verbose_name="S.17 Quel est le PREMIER onglet à ouvrir pour trouver l'outil?")
    prem_onglet_autre = models.CharField(blank=True, null=True, max_length=200, verbose_name="Si autre, précisez")
    deuxieme_onglet = models.CharField(choices=DEUX_ONGLET_LIST,
                                       max_length=200,
                                       default="Ne s'applique pas",
                                       null=True,
                                       verbose_name="S.18 Quel est le DEUXIEME onglet à ouvrir pour trouver l'outil?")
    deux_onglet_autre = models.CharField(blank=True, null=True, max_length=200, verbose_name="Si autre, précisez")
    troisieme_onglet = models.CharField(choices=TROIS_ONGLET_LIST,
                                        max_length=200,
                                        default="Ne s'applique pas",
                                        null=True,
                                        verbose_name="S.19 Quel est le TROISIEME onglet à ouvrir pour trouver l'outil?")
    trois_onglet_autre = models.CharField(blank=True, null=True, max_length=200, verbose_name="Si autre, précisez")

    mode_hebergement = models.ManyToManyField(ModeHebergement, verbose_name="S.20 Mode d'hébergement sur la toile")
    mode_consultation = models.ManyToManyField(ModeConsultation, verbose_name="S.21 Mode de consultation offert au public")
    narration_langue = models.ManyToManyField(LangueNarration, verbose_name="S.22 Langue de la narration")
    sous_titre = models.ManyToManyField(SousTitre, verbose_name="S.23 Sous-titrage")

    ##Accessibilité
    malentendants = models.CharField(choices=OUINON,
                                     max_length=200,
                                     null=False,
                                     default="Non",
                                     verbose_name="S.24.1 Cet outil est-il accessible aux malentendants (Sous titrage, language des signes)")
    malvoyants = models.CharField(choices=OUINON,
                                  max_length=200,
                                  null=False,
                                  default="Non",
                                  verbose_name="S.24.2 Cet outil est-il accessible aux malvoyants (audiodescription)")
    ## Quid du materiau musical
    materiau_musical = models.CharField(choices=OUINON,
                                        max_length=200,
                                        default="Non",
                                        verbose_name="M.25 Parle-t-on du matériau musical?")
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
                                      verbose_name="M.27.2 Parle-t-on du contexte de composition, création, interprétation de l'oeuvre, de l'instrument...")
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
