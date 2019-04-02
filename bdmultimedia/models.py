# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from multiselectfield import MultiSelectField
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django_currentuser.db.models import CurrentUserField
# from django.template.defaultfilters import slugify
from sortedm2m.fields import SortedManyToManyField


PROGRAMMATION_LIST = (
    ("Je n'ai pas de programmation", "Je n'ai pas de programmation"),
    ("Oui, en lien avec la programmation de concert", "Oui, en lien avec la programmation de concert"),
    ("Oui, en lien avec la programmation pédagogique", "Oui, en lien avec la programmation pédagogique"),
    ("Non", "Non"),
)

DUREE_LIST = (
    ("Un mois ou moins","Un mois ou moins"),
    ("Entre deux et six mois","Entre deux et six mois"),
    ("Entre six mois et un an","Entre six mois et un an"),
    ("Entre deux et cinq ans","Entre deux et cinq ans"),
    ("Plus de cinq ans","Plus de cinq ans"),
    ("De façon permanente","De façon permanente")
)


MEDIATEUR_LIST = (
    ("Oui, à temps plein","Oui, à temps plein"),
    ("Oui, à temps partiel","Oui, à temps partiel"),
    ("Non", "Non"),
    ("Ne sais pas","Ne sais pas")
)

SOUS_TRAITANT_LIST = (
    ("Oui, entièrement", "Oui, entièrement"),
    ("Oui, en partie","Oui, en partie"),
    ("Non", "Non")
)

FORME_DELEGATION_LIST = (
    ("Sous-traitance","Sous-traitance"),
    ("Collaboration (avec une école professionnelle, avec une start up, etc.)", "Collaboration (avec une école professionnelle, avec une start up, etc.)"),
    ("Partenariat (publicitaire, de recherche, etc.)","Partenariat (publicitaire, de recherche, etc.)"),
    ("Mecenat (réalisé grâce bénévolat d'employés d'une entreprise privée)", "Mecenat (réalisé grâce bénévolat d'employés d'une entreprise privée)"),
    ("Autre", "Autre")
)

USAGER_LIST = (
    ("Grand public", "Grand public"),
    ("Vos abonnés actuels", "Vos abonnés actuels"),
    ("D'anciens abonnés","D'anciens abonnés"),
    ("Les détenteurs de billets","Les détenteurs de billets"),
    ("Les groupes scolaires","Les groupes scolaires"),
    ("Organismes sociocommunautaires", "Organismes sociocommunautaires"),
    ("Les abonnés de vos médias sociaux", "Les abonnés de vos médias sociaux"),
    ("Nouveau public", "Nouveau public"),
    ("Aucun rapport avec mon organime", "Aucun rapport avec mon organime"),
    ("Autre","Autre")
)

PUBLIC_CIBLE_LIST = (
    ("Pas de public cible","Pas de public cible"),
    ("Nourisson et petite enfance (0 à 3 ans)","Nourisson et petite enfance (0 à 3 ans)"),
    ("Enfants (4 à 12 ans)","Enfants (4 à 12 ans)"),
    ("Adolescents (13 à 16 ans)","Adolescents (13 à 16 ans)"),
    ("Adulescents (16 à 18 ans)","Adulescents (16 à 18 ans)"),
    ("Jeunes actifs (19 à 25 ans)","Jeunes actifs (19 à 25 ans)"),
    ("Actifs (25 à 65 ans)","Actifs (25 à 65 ans)"),
    ("Retraités -(plus de 65 ans)","Retraités -(plus de 65 ans)")
)

ACTION_LIST = (
    ("D'éducation musicale","D'éducation musicale"),
    ("De développement de public","De développement de public"),
    ("Publicitaire et promotionnelle","Publicitaire et promotionnelle"),
    ("De médiation de la musique", "De médiation de la musique"),
    ("Autre", "Autre")
)

OUINON = (
    ("Oui", "Oui"),
    ("Non", "Non"),
)

OUINONNSP = (
    ("Oui", "Oui"),
    ("Non", "Non"),
    ("Nsp", "Ne s'applique pas")
)

INTERACTIVITE_LIST = (
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
    ("Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation","Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format du dispositif dont il s'agit", "Est relatif au format du dispositif dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("Relatif au site d'hébergement","Est relatif au site d'hébergement"),
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
    ("Relatif au site d'hébergement", "Est relatif au site d'hébergement"),
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
    ("Ressources en ligne, ressources numériques, ressources", "Ressources en ligne, ressources numériques, ressources"),
    ("Relatif à la programmation",
     "Est relatif à la programmation à laquelle il fait référence (onglet du concert, titre du compositeur, etc.)"),
    ("Relatif au format du dispositif dont il s'agit",
     "Est relatif au format du dispositif dont il s'agit (Balado, vidéo, playlist, web série, etc.)"),
    ("Relatif au site d'hébergement", "Est relatif au site d'hébergement"),
    ("À propos", "À propos"),
    ("Voir et entendre", "Voir et entendre"),
    ("Actualités, news, nouveauté", "Actualité, news, nouveauté"),
    ("Pour tous les publics", "Pour tous les publics"),
    ("Pour un public spécifique", "Pour un public spécifique"),
    ("Musique", "Musique"),
    ("Autre", "Autre")
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
        verbose_name = "type de producteur"
        verbose_name_plural = "types de producteur"


@python_2_unicode_compatible
class ProducteurNom(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Nom du producteur"
        verbose_name_plural = "Noms des producteurs"


@python_2_unicode_compatible
class SupportDiffusion(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "support de diffusion"
        verbose_name_plural = "supports de diffusion"


@python_2_unicode_compatible
class FormeNarrative(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Forme narrative"
        verbose_name_plural = "Formes narratives"


@python_2_unicode_compatible
class ModeHebergement(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Mode d'hébergement sur la toile"
        verbose_name_plural = "Modes d'hébergement sur la toile"


@python_2_unicode_compatible
class ModeConsultation(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Mode de consultation offert au public"
        verbose_name_plural = "Modes de consultation offerts au public"


@python_2_unicode_compatible
class LangueNarration(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Langue de la narration"
        verbose_name_plural = "Langues de narration"


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
        verbose_name = "Son et orchestration"
        verbose_name_plural = "Sons et orchestrations"


@python_2_unicode_compatible
class Structure(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Structure"


@python_2_unicode_compatible
class LanguageMusical(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Language musical"
        verbose_name_plural = "Languages musicaux"


@python_2_unicode_compatible
class GenreMusical(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Genre musical"
        verbose_name_plural = "Genres musicaux"


@python_2_unicode_compatible
class StyleMusical(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Style musical"
        verbose_name_plural = "Styles musicaux"


@python_2_unicode_compatible
class ExperienceMusicale(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Experience musicale"
        verbose_name_plural = "Experiences musicales"


@python_2_unicode_compatible
class Epoque(models.Model):
    nom = models.CharField(max_length=200, unique = True)

    def __str__(self):
        return self.nom


@python_2_unicode_compatible
class Contexte(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Contexte de composition, création, interprétation..."
        verbose_name_plural = "Contextes de composition, création, interprétation..."


@python_2_unicode_compatible
class RoleEvolution(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Rôle et évolution du métier"
        verbose_name_plural = "Rôles et évolutions des métiers"


@python_2_unicode_compatible
class Organologie(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Organologie"


@python_2_unicode_compatible
class SollicitationMusicale(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Sollicitation musicale"
        verbose_name_plural = "Sollicitations musicales"


@python_2_unicode_compatible
class SollicitationGenerale(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Sollicitation générale"
        verbose_name_plural = "Sollicitations générales"


@python_2_unicode_compatible
class EvocationGraphique(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Évocation graphique"
        verbose_name_plural = "Évocations graphiques"


@python_2_unicode_compatible
class EvocationPlastique(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Évocation plastique"
        verbose_name_plural = "Évocations plastiques"


@python_2_unicode_compatible
class EvocationAutre(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Évocation d'autre discipline"
        verbose_name_plural = "Évocations d'autres disciplines"


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
        verbose_name = "Role des humains indéterminé"


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
        verbose_name_plural = "Formats de dispositif"


@python_2_unicode_compatible
class NotionsInter(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Exemple de notion évoquée de façon interdisciplinaire"
        verbose_name_plural = "Exemples de notions évoquées de façon interdisciplinaires"

@python_2_unicode_compatible
class Query(models.Model):
    nom = models.CharField(max_length=400, unique= False)
    temps = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return "/recherche_motcle/?csrfmiddlewaretoken={{ csrf_token }}&q=%s" % self.nom




# Pour la recherche par mots-clés
class OutilManager(models.Manager):
    def search(self, query=None):
        liste_q = []
        for i in list(Query.objects.values_list('nom')):
            liste_q.append(i[0])

        if query not in liste_q:
            new = Query(nom=query)
            new.save()

        qs = self.get_queryset().prefetch_related('producteur_type','producteur_nom','support_diffusion','format','forme_narrative',
                                                  'mode_hebergement','narration_langue','sous_titre','orchestration','structure',
                                                  'language_musical', 'genre_musical', 'style_musical', 'experience_musicale',
                                                  'contexte', 'role_evolution','organologie','sollicitation_musicale',
                                                  'sollicitation_generale','evocation_graphique','evocation_plastique',
                                                  'evocation_autre', 'exemples_notions_interdisciplinaires',
                                                  'role_humain_femme', 'role_humain_homme', 'role_humain_neutre',
                                                  'role_pers_anime_femme', 'role_pers_anime_homme',
                                                  'role_pers_anime_neutre', 'role_animaux_femme', 'role_animaux_homme')
        if query is not None:
            # maximum 64 tables en sqlite
            or_lookup = (Q(titre__icontains=query) |
                         Q(url__icontains=query) |
                         Q(site__icontains=query) |
                         Q(ensemble_thematique_nom__icontains=query) |
                         Q(interactivite__icontains=query) |
                         # Q(elements_socioculturels__icontains=query) |
                         Q(epoque__nom__icontains=query) |
                         Q(producteur_type__nom__icontains=query) |
                         Q(producteur_nom__nom__icontains=query) |
                         #? Q(support_diffusion__nom__icontains=query) |
                         #? Q(format__nom__icontains=query) |
                         Q(forme_narrative__nom__icontains=query) |
                         Q(mode_hebergement__nom__icontains=query) |
                         # Q(narration_langue__nom__icontains=query) |
                         # Q(sous_titre__nom__icontains=query) |
                         Q(orchestration__nom__icontains=query) |
                         Q(structure__nom__icontains=query) |
                         Q(language_musical__nom__icontains=query) |
                         Q(genre_musical__nom__icontains=query) |
                         Q(style_musical__nom__icontains=query) |
                         Q(experience_musicale__nom__icontains=query) |
                         Q(contexte__nom__icontains=query) |
                         Q(role_evolution__nom__icontains=query) |
                         Q(organologie__nom__icontains=query) |
                         Q(sollicitation_musicale__nom__icontains=query) |
                         Q(sollicitation_generale__nom__icontains=query) |
                         Q(evocation_graphique__nom__icontains=query) |
                         Q(evocation_plastique__nom__icontains=query) |
                         Q(evocation_autre__nom__icontains=query) |
                         Q(exemples_notions_interdisciplinaires__nom__icontains=query) |
                         Q(role_humain_femme__nom__icontains=query) |
                         Q(role_humain_homme__nom__icontains=query) |
                         Q(role_humain_neutre__nom__icontains=query) |
                         Q(role_pers_anime_femme__nom__icontains=query) |
                         Q(role_pers_anime_homme__nom__icontains=query) |
                         Q(role_pers_anime_neutre__nom__icontains=query) |
                         # Q(role_animaux_femme__nom__icontains=query) |
                         Q(role_animaux_homme__nom__icontains=query) # |
                         # Q(role_animaux_neutre__nom__icontains=query) |
                         # Q(role_instr_anime_femme__nom__icontains=query) |
                         # Q(role_instr_anime_homme__nom__icontains=query)# |
                         # Q(role_instr_anime_neutre__nom__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct().order_by('titre')
        return qs


@python_2_unicode_compatible
class Outil(models.Model):

    # RÉFÉRENCEMENT
    titre = models.CharField(max_length=200, verbose_name="R.1 Titre du dispositif", db_index=True,
                             help_text = "Tout support disponible en ligne ne perdant rien à être imprimé n’entre pas dans le corpus analysé ici.")
    page_outil = models.BooleanField(default = False, verbose_name = "Afficher directement une page qui fait office de dispositif")
    integration = models.TextField(blank = True, verbose_name = "code pour l'integration du dispositif (si applicable)")
    url = models.CharField(db_index=True, unique=True, max_length=200, verbose_name="R.2 URL d'accès direct",
                           help_text="Attention, enlever la barre oblique « / » à la fin de l’URL Ex. www.osm.ca/fr/matinees/#1488205065259-011decba-7105")
    site = models.CharField(db_index=True, max_length=200, verbose_name="R.3 URL d'accès au site d'hébergement",
                           help_text="Attention, enlever la barre oblique « / » à la fin de l’URL www.osm.ca. Si le dispositif est une vidéo d’un-e YouTubeur-e, indiquer le lien vers sa chaîne YouTube.")
    ensemble_thematique = models.CharField(blank=False, choices=OUINON, max_length=4, default="Non",
                                           verbose_name="R.3.1 Ce dispositif fait-il partie d'un ensemble thématique du même type? (regroupé par l'organisme producteur)",
                                           help_text = "On parle bien ici d’un ensemble thématique et non pas d’un regroupement par format (ex. vidéo) ou par objectif (ex . ressource pédagogique). ")
    ensemble_thematique_nom = models.CharField(db_index=True, max_length=200, verbose_name="R.3.2 Si oui, donnez le titre sous lequel est regroupé cet ensemble.",
                                               blank=True, help_text="Ex: Camille raconte")
    producteur_type = models.ManyToManyField(ProdType, db_index=True,  verbose_name="R.4 Qui est le producteur de ce dispositif?",
                                             help_text = "Attention : répondre à cette question nécessite d’aller vérifier les statuts des organismes impliqués ou le titre auquel ils s’impliquent. Exemple . L’OSM peut agir en tant que producteur pour un concert ou au titre de diffuseur pour un autre évènement.")
    producteur_nom = models.ManyToManyField(ProducteurNom, db_index=True, verbose_name="R.5 Préciser le nom complet du/des producteur(s)")
    support_diffusion = models.ManyToManyField(SupportDiffusion, db_index=True, verbose_name="R.6 Support de diffusion")
    format = models.ManyToManyField(FormatOutil, db_index=True, verbose_name="R.7 Format du dispositif")

    forme_narrative = SortedManyToManyField(FormeNarrative, db_index=True, verbose_name="R.8 Formes narratives")

    duree = models.CharField(max_length=8, null=False, verbose_name="R.9 Durée", default="00:00:00",
                             help_text="nsp = ne s'applique pas, ddv = durée d’écoute variable. La durée d’écoute est variable puisque les utilisateurs peuvent décider, ou non, de regarder les vidéos. Concerne les dispositifs qui allient texte et vidéo.")
    nb_pages = models.CharField(null=True, verbose_name="R.10 Nombre de pages",
                                            max_length = 16,
                                           help_text="Correspond au nombre de page web sur lesquelles se décline le  dispositif. Nsp = ne s'applique pas. Si plus que 20 pages, inscrire : plus de 20 pages")
    mise_en_ligne_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False,
                                          verbose_name="R.11 Date de la mise en ligne",
                                          help_text="Si seule l’année de mise en ligne est disponible entrer la date de mise en ligne au 1er janvier de l’année concernée. Si la date n'est pas disponible, laisser vide.")
    depouillement_date = models.DateField(null=True, blank=False, auto_now=False, auto_now_add=False,
                                          verbose_name="R.12 Date du dépouillement")
    interactivite = models.CharField(db_index=True, choices=INTERACTIVITE_LIST,
                                 max_length=200,
                                 null=True,
                                 verbose_name="R.13 Interactivité")
    materiel_imprimer = models.CharField(choices=OUINON, max_length = 200, default = "Non",
                                         verbose_name = "R.13.1 Le dispositif comprend-il du matériel à imprimer (ex. livret en pdf) ?")
    personnification_service = models.CharField(null=True, max_length=200, choices=PERSONNIFICATION_LIST,
                                                verbose_name="R.14 Degrés de personnification du service")
    commentaire_possible = models.BooleanField(verbose_name="R.15 Possibilité de laisser des commentaires",
                                               help_text="Compter les commentaires qui apparaissent sur la page de consultation du dispositif (ex. Si il n’y a pas de possibilité de commentaire sur les capsules de l’OSM mais que les commentaires sont possibles sur l’hébergement youtube ne pas cocher)")
    commentaire_nombre = models.CharField(max_length = 50,null=True, blank=True, verbose_name="R.16 Nombre de commentaires")

    # DÉCOUVRABILITÉ / ACCESSIBILITÉ
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

    mode_hebergement = models.ManyToManyField(ModeHebergement, db_index=True,  verbose_name="S.20 Mode d'hébergement sur la toile")
    mode_consultation = models.ManyToManyField(ModeConsultation, verbose_name="S.21 Mode de consultation offert au public")
    narration_langue = models.ManyToManyField(LangueNarration, db_index=True,  verbose_name="S.22 Langue du dispositif")
    sous_titre = models.ManyToManyField(SousTitre, db_index=True,  verbose_name="S.23 Sous-titrage",
                                        help_text="Les sous-titrages automatiques proposés par YouTube n’entrent pas en considération.")
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

    # DISCOURS SUR LA MUSIQUE
    #### Analyses musicales
    materiau_musical = models.CharField(choices=OUINON,
                                        max_length=200,
                                        default="Non",
                                        verbose_name="M.25 Parle-t-on du matériau musical?")
    orchestration = models.ManyToManyField(Orchestration, db_index=True, default = 1,
                                           verbose_name="M.25.1 Parle-t-on du son et de l'orchestration, si oui précisez.",
                                           help_text='Registres (au sens de groupe de hauteur si cela concerne les registres de l’orgue cocher « timbres »)')
    structure = models.ManyToManyField(Structure, db_index=True, default = 1,
                                       verbose_name="M.25.2 Parle-t-on de la structure, si oui précisez.")
    language_musical = models.ManyToManyField(LanguageMusical, db_index=True, default = 1,
                                              verbose_name="M.25.3 Parle-t-on du language musical, si oui précisez.")
    genre_musical = models.ManyToManyField(GenreMusical, db_index=True, default = 1,
                                           verbose_name="M.25.4 Parle-t-on du genre musical, si oui précisez.")
    style_musical = models.ManyToManyField(StyleMusical, db_index=True, default = 1,
                                           verbose_name="M.25.5 Parle-t-on du style musical, si oui précisez.")
    #### Éléments contextuels
    experience_musicale = models.ManyToManyField(ExperienceMusicale, db_index=True,
                                                 verbose_name="M.26 Parle-t-on de l'experience musicale, si oui précisez.")
    elements_socioculturels = models.CharField(choices=OUINON,
                                               max_length=200,
                                               default="Non",
                                               verbose_name="M.27 Parle-t-on des éléments socioculturels et historiques?")

    epoque = models.ManyToManyField(Epoque, db_index=True,
                                        verbose_name="M.27.1 Époque", help_text="Inscrire les époques évoquées dans le dispositif (non pas l’époque de tournage du dispositif).<br> Cocher une époque seulement lorsqu'elle est développée. Si un phénomène musical est évoqué de façon transversale et dispersée dans le temps, sans focus, cocher \"hors temps\", un dispositif peut se retrouver dans une case \"temporelle\" et \"hors temps\" cf. <a href = https://www.youtube.com/watch?v=fSKBwjWE7NQ target='_blank'>https://www.youtube.com/watch?v=fSKBwjWE7NQ</a>")

    contexte = models.ManyToManyField(Contexte, db_index=True,
                                      verbose_name="M.27.2 Parle-t-on du contexte de composition, création, interprétation de l'oeuvre, de l'instrument...",
                                      help_text='Si il est juste fait mention d’une date sans donner plus d’information sur ce qui se passait à l’époque cocher “Non”.')
    role_evolution = models.ManyToManyField(RoleEvolution, db_index=True,
                                            verbose_name="M.27.3 Parle-t-on du rôle et de l'évolution du [métier liés à la musique précisez]")
    organologie = models.ManyToManyField(Organologie, db_index=True,
                                         verbose_name = "M.27.4 Parle-t-on d’organologie?")

    # SOLLICITATIONS DE L'USAGER
    sollicitation_musicale = models.ManyToManyField(SollicitationMusicale, db_index=True,
                                                    verbose_name="U.28 Pour comprendre le discours sur la musique")
    sollicitation_generale = models.ManyToManyField(SollicitationGenerale, db_index=True,
                                                    verbose_name="U.29 Pour comprendre le discours général")

    # PLACE DE LA MUSIQUE
    temps_mus = models.CharField(max_length=8, null=False, verbose_name="PM.30 Temps de musique seule (hh:mm:ss)",
                                 default="00:00:00",
                                 help_text="ddv = durée d’écoute variable. Concerne les dispositifs qui allient texte et vidéo. La durée d’écoute est variable puisque les utilisateurs peuvent décider, ou non, de regarder les vidéos.<br> 00.00.00 =  signifie qu’il y a bien du son dans le dispositif.<br> nsp signifie qu’il n’y a pas de son dans le dispositif.")
    temps_par = models.CharField(max_length=8, null=False, verbose_name="PM.31 Temps de parole seule (hh:mm:ss)",
                                 default="00:00:00", help_text="ddv = durée d’écoute variable. Concerne les dispositifs qui allient texte et vidéo. La durée d’écoute est variable puisque les utilisateurs peuvent décider, ou non, de regarder les vidéos. <br> nsp = ne s'applique pas")
    temps_mus_par = models.CharField(max_length=8, null=False,
                                     verbose_name="PM.32 Temps de parole et musique superposées (hh:mm:ss)",
                                     default="00:00:00", help_text="ddv = durée d’écoute variable. Concerne les dispositifs qui allient texte et vidéo. La durée d’écoute est variable puisque les utilisateurs peuvent décider, ou non, de regarder les vidéos.<br> nsp = ne s'applique pas")
    sonore_valeur = models.CharField(choices=SONORE_VALEUR_LIST,
                                     max_length=200,
                                     null=False,
                                     default="Nsp",
                                     verbose_name="PM.33 Mise en valeur du sonore")

    # ÉVOCATION DE LA MUSIQUE EXTRA-SONORE
    evocation_graphique = models.ManyToManyField(EvocationGraphique, db_index=True,
                                           verbose_name="EM.34 Évocation graphique")
    evocation_plastique = models.ManyToManyField(EvocationPlastique, db_index=True,
                                           verbose_name="EM.35 Évocation plastique")
    evocation_litteraire = MultiSelectField(choices=EVOCATION_LITTERAIRE_LIST,
                                            max_length=200,
                                            null=False,
                                            verbose_name="EM.36 Évocation littéraire",
                                            help_text= 'Le matériau musical est-il décrit “en mots” dans le dispositif ?')

    # INTERDISCIPLINARITÉ
    evocation_autre = models.ManyToManyField(EvocationAutre, db_index=True,
                                       verbose_name="I.37 Autres disciplines évoquées?")
    ####à partir de quelle notion?
    notion_concepts = models.CharField(choices = OUINONNSP,
                                       max_length = 20,
                                       null = False,
                                       default = "Nsp",
                                       verbose_name="I.38 À partir de quelle notion? - Notions communes (luminosité, transparence, vitesse, mouvement)")
    notion_experiences = models.CharField(choices = OUINONNSP,
                                       max_length = 20,
                                       null = False,
                                       default = "Nsp",
                                       verbose_name="I.38 À partir de quelle notion? - Expérience (émotions)")
    notion_pratiques = models.CharField(choices = OUINONNSP,
                                       max_length = 20,
                                       null = False,
                                       default = "Nsp",
                                       verbose_name="I.38 À partir de quelle notion? - Pratique (processus de création)")
    exemples_notions_interdisciplinaires = models.ManyToManyField(NotionsInter, db_index=True,
                                                                  blank = True,
                                                                  verbose_name="I.39 Donner des exemples de notions évoquées de façon interdisciplinaires")

    # STÉRÉOTYPES DE GENRE
    nb_humains_total = models.CharField(verbose_name="Sté.39.1 Nombre d'humains total",
                                        max_length = 10,
                                        default = "0",
                                        help_text = 'On compte tous les humains qui sont 3 ou moins dans le cadre. Si le nombre excède 11, écrire "11 et plus"')
    nb_femmes = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre de femmes", default=0)
    nb_hommes = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre d'hommes", default=0)
    nb_humains_indetermines = models.PositiveIntegerField(verbose_name="Sté.39.1 Nombre d'humains au genre indéterminé",
                                                          default=0)
    role_humain_femme = models.ManyToManyField(RoleFemmes, db_index=True,
                                               verbose_name="Sté.39.2 Rôle des femmes", default = 1)
    role_humain_homme = models.ManyToManyField(RoleHomme, db_index=True,
                                                verbose_name="Sté.39.3 Rôle des hommes", default = 1)
    role_humain_neutre = models.ManyToManyField(RoleHumainNeutre, db_index=True,
                                                verbose_name="Sté.39.4 Rôle des indéterminés", default = 1)
    nb_pers_anime_total = models.CharField(null = True, verbose_name="Sté.40.1 Nombre de personnages animés total",
                                           max_length=10,
                                           default="0",
                                           help_text='Si le nombre excède 11, écrire "11 et plus"')
    nb_pers_anime_femmes = models.PositiveIntegerField(null=True,
                                                       verbose_name="Sté.40.1 Nombre de personnages animés femmes",
                                                       default=0)
    nb_pers_anime_hommes = models.PositiveIntegerField(null=True, verbose_name="Sté.40.1 Nombre de personnages animés hommes",
                                                       default=0)
    nb_pers_anime_indetermines = models.PositiveIntegerField(null=True,
                                                             verbose_name="Sté.40.1 Nombre de personnages animés au genre indéterminé",
                                                             default=0)
    role_pers_anime_femme = models.ManyToManyField(RolePersAnimFemmes, db_index=True,
                                                   verbose_name="Sté.40.3 Rôle des personnages animés féminins", default = 1)
    role_pers_anime_homme = models.ManyToManyField(RolePersAnimHomme, db_index=True,
                                                   verbose_name="Sté.40.2 Rôle des personnages animés masculins", default = 1)
    role_pers_anime_neutre = models.ManyToManyField(RolePersAnimNeutre, db_index=True,
                                                    verbose_name="Sté.40.4 Rôle des personnages animés indéterminés", default = 1)
    nb_animaux_total = models.CharField(null = True, verbose_name="Sté.41.1 Nombre d'animaux total",
                                        max_length=10,
                                        default="0",
                                        help_text='Si le nombre excède 11, écrire "11 et plus"')
    nb_femelles = models.PositiveIntegerField(null=True, verbose_name="Sté.41.1 Nombre de femelles", default=0)
    nb_males = models.PositiveIntegerField(null=True, verbose_name="Sté.41.1 Nombre de mâles", default=0)
    nb_animaux_indetermines = models.PositiveIntegerField(null=True,
                                                          verbose_name="Sté.41.1 Nombre d'animaux au genre indéterminé",
                                                          default=0)
    role_animaux_femme = models.ManyToManyField(RoleAnimauxFemmes, db_index=True,
                                                verbose_name="Sté.41.3 Rôle des animaux femelles", default = 1)
    role_animaux_homme = models.ManyToManyField(RoleAnimauxHomme, db_index=True,
                                                verbose_name="Sté.41.2 Rôle des animaux mâles", default = 1)
    role_animaux_neutre = models.ManyToManyField(RoleAnimauxNeutre, db_index=True,
                                                 verbose_name="Sté.41.4 Rôle des animaux indéterminés", default = 1)
    nb_instr_anime_total = models.CharField(null=True, verbose_name="Sté.42.1 Nombre d'instruments animés total",
                                            max_length=10,
                                            default="0",
                                            help_text='cf. anthropomorphe. Si le nombre excède 11, écrire "11 et plus"')
    nb_instr_anime_femmes = models.PositiveIntegerField(null=True,
                                                        verbose_name="Sté.42.1 Nombre d'instruments animés féminins",
                                                        default=0)
    nb_instr_anime_hommes = models.PositiveIntegerField(null=True, verbose_name="Sté.42.1 Nombre d'instruments animés masculins",
                                                        default=0)
    nb_instr_anime_indetermines = models.PositiveIntegerField(null=True,
                                                              verbose_name="Sté.42.1 Nombre d'instruments animés au genre indéterminé",
                                                              default=0)
    role_instr_anime_femme = models.ManyToManyField(RoleInstrFemmes, db_index=True,
                                                    verbose_name="Sté.42.3 Rôle des instruments anthropomorphes féminins", default = 1)
    role_instr_anime_homme = models.ManyToManyField(RoleInstrHomme, db_index=True,
                                                    verbose_name="Sté.42.2 Rôle des instruments anthropomorphes masculins", default = 1)
    role_instr_anime_neutre = models.ManyToManyField(RoleInstrNeutre, db_index=True,
                                                     verbose_name="Sté.42.4 Rôle des instruments anthropomorphes neutres", default = 1)

    # AJOUT dec 2018
    email = models.EmailField(verbose_name="Addresse courriel", null=True, blank=True)
    organisme = models.CharField(max_length=400, verbose_name="Quel est le nom de l'organisme que vous représentez ?",
                                 null=True, blank=True)
    outil_nom = models.CharField(max_length=400,
                                 verbose_name="Quel le nom de l'outil à propos duquel vous allez remplir ce questionnaire ?",
                                 null=True, blank=True)
    lien = models.URLField(verbose_name="Lien internet vers cet outil", null=True, blank=True)
    programmation = MultiSelectField(choices=PROGRAMMATION_LIST,
                                     verbose_name="Cet outil a-t-il été conçu en lien avec votre programmation ?",
                                     default="Non", blank=True)
    duree_conception = models.CharField(max_length=50, choices=DUREE_LIST,
                                        verbose_name="La conception du contenu de ce outil a été de", null=True, blank=True)
    duree_realisation = models.CharField(max_length=50, choices=DUREE_LIST,
                                         verbose_name="La durée du travail nécessaire à sa réalisation/production a été de",
                                         null=True, blank=True)
    duree_disponibilite = models.CharField(max_length=50, choices=DUREE_LIST,
                                           verbose_name="Sa disponibilité en ligne est prévue pour durer", null=True, blank=True)
    mediateur_professionnel = models.CharField(max_length=50, choices=MEDIATEUR_LIST,
                                               verbose_name="Avez-vous fait appel à un médiateur professionnel ou à quelqu'un dont les tâches sont associées aux activités de médiation (de votre organisme ou indépendant) pour concevoir ce dispositif ?",
                                               null=True, blank=True)
    iniciateur = models.CharField(max_length=400,
                                  verbose_name="Quelles étaient les personnes à l'initiative de ce projet ? Donner leur fonction et leur statut (ex. le/la responsable du développement des publics)",
                                  null=True, blank=True)
    responsable = models.CharField(max_length=400,
                                   verbose_name="Quels étaient les responsables de ce projet ? Donner leur fonction et leur statut ( ex. un.e stagiaire du département marketing)",
                                   null=True, blank=True)
    sous_traitant = models.CharField(max_length=20, choices=SOUS_TRAITANT_LIST,
                                     verbose_name="Avez-vous confié la réalisation/production de cet outil à des personnes extérieures à votre organisme ?",
                                     null=True, blank=True)
    forme_delegation = MultiSelectField(max_length=400, choices=FORME_DELEGATION_LIST,
                                        verbose_name="Quelle forme a pris la délégation de la réalisation/production de cet outil ?",
                                        null=True, blank=True)
    forme_delegation_autre = models.CharField(max_length=400, verbose_name="Autre, précisez.", null=True, blank=True)
    realisateur = models.CharField(max_length=400,
                                   verbose_name="Qui a réalisé/produit ce projet ? (nom de l'entreprise si il y a lieu, sinon, fonction et statut du responsable de la mise en œuvre du projet)",
                                   null=True, blank=True)
    cout = models.PositiveIntegerField(
        verbose_name="Quel est le coût approximatif de la réalisation/production de cet outil ? (en nombre ex: 2000$)",
        default=0, blank=True)
    usager = MultiSelectField(max_length=400,
                              verbose_name=" Quel est le rapport entre les usagers que vous imaginiez pour ce dispositif et votre organisme ?",
                              null=True, blank=True)
    action_utilisateurs = models.TextField(
        verbose_name="Complétez cette phrase : en créant ce dispositif notre objectif était que ses utilisateurs...",
        null=True, blank=True)
    public_cible = MultiSelectField(max_length=300, choices=PUBLIC_CIBLE_LIST,
                                    verbose_name="Quelle est la tranche d'âge du public cible de cet outil ?",
                                    null=True, blank=True)
    action = MultiSelectField(max_length=200, choices=ACTION_LIST,
                              verbose_name="Cet outil sert une action (plusieurs choix possibles)", null=True, blank=True)
    action_delegation_autre = models.CharField(max_length=400, verbose_name="Autre, précisez.", null=True, blank=True)

    utilisateur = CurrentUserField(editable = False)

    objects = OutilManager()

    def save(self):
        if "vimeo" in self.integration and "<p" in self.integration:
            self.integration = self.integration[0:self.integration.find('<p')]

        # if "youtu" in self.url and "?rel=0&amp;showinfo=0" not in self.integration:
            # self.integration = self.integration[:79] + '?rel=0&amp;showinfo=0' + self.integration[79:]

        if "border:none;" in self.integration:
            self.integration = self.integration.replace("border:none;", "")

        super(Outil, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return self.titre