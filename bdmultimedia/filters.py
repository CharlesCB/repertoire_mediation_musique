# -*- coding: utf-8 -*-

import django_filters
from django.db.models.fields import BLANK_CHOICE_DASH
from .models import *


class OutilFilter(django_filters.FilterSet):

    FORMAT_CHOICES = list(FormatOutil.objects.all().values_list("nom","nom"))

    FORME_NARRATIVE_CHOICES = list(FormeNarrative.objects.values_list("nom","nom"))

    PRODUCTEUR_TYPE_CHOICES = list(ProdType.objects.values_list("nom","nom"))

    SUPPORT_DIFFUSION_CHOICES = list(SupportDiffusion.objects.values_list("nom","nom"))

    LANGUE_CHOICES = list(LangueNarration.objects.exclude(nom = "Ne s'applique pas").values_list("nom","nom"))

    MODE_CONSULTATION_CHOICES = list(ModeConsultation.objects.values_list("nom","nom"))

    SONORE_VALEUR_CHOICES = list(SONORE_VALEUR_LIST)
    del SONORE_VALEUR_CHOICES[0]

    EVOCATION_LITTERAIRE_CHOICES =  list(EVOCATION_LITTERAIRE_LIST)
    del EVOCATION_LITTERAIRE_CHOICES[0]

    EVOCATION_GRAPHIQUE_CHOICES = list(EvocationGraphique.objects.exclude(nom="Non").values_list("nom","nom"))

    EVOCATION_PLASTIQUE_CHOICES = list(EvocationPlastique.objects.exclude(nom="Non").values_list("nom", "nom"))

    ORCHESTRATION_CHOICES = list(Orchestration.objects.exclude(nom="Non").values_list("nom","nom"))

    STRUCTURE_CHOICES = list(Structure.objects.exclude(nom="Non").values_list("nom", "nom"))

    LANGUAGE_MUSICAL_CHOICES = list(LanguageMusical.objects.exclude(nom="Non").values_list("nom", "nom"))

    GENRE_MUSICAL_CHOICES = list(GenreMusical.objects.exclude(nom="Non").values_list("nom", "nom"))

    STYLE_MUSICAL_CHOICES = list(StyleMusical.objects.exclude(nom="Non").values_list("nom", "nom"))

    EXPERIENCE_MUSICALE_CHOICES = list(ExperienceMusicale.objects.exclude(nom="Non").values_list("nom", "nom"))

    CONTEXTE_CHOICES = list(Contexte.objects.exclude(nom="Non").values_list("nom","nom"))

    ROLE_EVOLUTION_CHOICES = list(RoleEvolution.objects.exclude(nom="Non").values_list("nom", "nom"))

    EPOQUE_CHOICES = Epoque.objects.values_list("nom","nom").order_by('nom')

    SOLLICITATION_MUSICALE_CHOICES = SollicitationMusicale.objects.values_list("nom","nom").order_by("nom")

    SOLLICITATION_GENERALE_CHOICES = SollicitationGenerale.objects.values_list("nom","nom").order_by("nom")

    DISCIPLINE_CHOICES = BLANK_CHOICE_DASH + list(EvocationAutre.objects.exclude(nom="Aucune").values_list('nom','nom'))

    NOTIONS_CONCEPT_CHOICES = BLANK_CHOICE_DASH + list(OUINONNSP)


    format__nom = django_filters.MultipleChoiceFilter(choices=FORMAT_CHOICES, lookup_expr='iexact')
    forme_narrative__nom = django_filters.MultipleChoiceFilter(choices=FORME_NARRATIVE_CHOICES,
                                                       lookup_expr="iexact")
    interactivite = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + list(INTERACTIVITE_LIST),
                                                lookup_expr='iexact')
    personnification_service = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + list(PERSONNIFICATION_LIST),
                                                           lookup_expr="iexact")
    producteur_type__nom = django_filters.MultipleChoiceFilter(choices=PRODUCTEUR_TYPE_CHOICES,
                                                       lookup_expr='iexact')
    support_diffusion__nom = django_filters.MultipleChoiceFilter(choices=SUPPORT_DIFFUSION_CHOICES,
                                                         lookup_expr='iexact')
    ensemble_thematique = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + list(OUINON),
                                                      lookup_expr="exact")
    narration_langue__nom = django_filters.MultipleChoiceFilter(choices=LANGUE_CHOICES, lookup_expr='iexact')
    mode_consultation__nom = django_filters.MultipleChoiceFilter(choices=MODE_CONSULTATION_CHOICES,
                                                         lookup_expr='iexact')
    sonore_valeur = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + SONORE_VALEUR_CHOICES,
                                                lookup_expr="exact")
    evocation_litteraire = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + EVOCATION_LITTERAIRE_CHOICES,
                                                       lookup_expr="iexact")
    evocation_graphique__nom = django_filters.MultipleChoiceFilter(choices=EVOCATION_GRAPHIQUE_CHOICES,
                                                           lookup_expr="iexact")
    evocation_plastique__nom = django_filters.MultipleChoiceFilter(choices=EVOCATION_PLASTIQUE_CHOICES,
                                                           lookup_expr="iexact")
    #ANALYSE MUSICALE
    orchestration__nom = django_filters.MultipleChoiceFilter(choices=ORCHESTRATION_CHOICES, lookup_expr = "iexact")
    structure__nom = django_filters.MultipleChoiceFilter(choices=STRUCTURE_CHOICES, lookup_expr="iexact")
    language_musical__nom = django_filters.MultipleChoiceFilter(choices=LANGUAGE_MUSICAL_CHOICES, lookup_expr="iexact")
    genre_musical__nom = django_filters.MultipleChoiceFilter(choices=GENRE_MUSICAL_CHOICES, lookup_expr="iexact")
    style_musical__nom = django_filters.MultipleChoiceFilter(choices=STYLE_MUSICAL_CHOICES, lookup_expr="iexact")

    #ÉLÉMENTS CONTEXTUELS
    experience_musicale__nom = django_filters.MultipleChoiceFilter(choices=EXPERIENCE_MUSICALE_CHOICES, lookup_expr="iexact")
    contexte__nom = django_filters.MultipleChoiceFilter(choices=CONTEXTE_CHOICES, lookup_expr="iexact")
    role_evolution__nom = django_filters.MultipleChoiceFilter(choices=ROLE_EVOLUTION_CHOICES, lookup_expr="iexact")
    epoque__nom = django_filters.MultipleChoiceFilter(choices=EPOQUE_CHOICES, lookup_expr="icontains")

    sollicitation_musicale__nom = django_filters.MultipleChoiceFilter(choices=SOLLICITATION_MUSICALE_CHOICES,
                                                                      lookup_expr="iexact")
    sollicitation_generale__nom = django_filters.MultipleChoiceFilter(choices=SOLLICITATION_GENERALE_CHOICES,
                                                                      lookup_expr="iexact")

    evocation_autre__nom = django_filters.MultipleChoiceFilter(choices=DISCIPLINE_CHOICES, lookup_expr="iexact")
    notion_concepts = django_filters.ChoiceFilter(choices=NOTIONS_CONCEPT_CHOICES, lookup_expr='iexact')
    notion_experiences = django_filters.ChoiceFilter(choices = list(OUINONNSP), lookup_expr="iexact")
    notion_pratiques = django_filters.ChoiceFilter(choices = BLANK_CHOICE_DASH + list(OUINONNSP), lookup_expr="iexact")

    class Meta:
        model = Outil
        fields = [
            'format__nom',
            'forme_narrative__nom',
            'interactivite',
            'personnification_service',
            'producteur_type__nom',
            'support_diffusion__nom',
            'narration_langue__nom',
            'mode_consultation__nom',
            'sonore_valeur',
            'evocation_litteraire',
            'evocation_graphique__nom',
            'evocation_plastique__nom',
            'orchestration__nom',
            'structure__nom',
            'language_musical__nom',
            'genre_musical__nom',
            'style_musical__nom',
            'experience_musicale__nom',
            'contexte__nom',
            'role_evolution__nom',
            'epoque__nom',
        ]

