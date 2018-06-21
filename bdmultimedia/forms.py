# -*- coding: utf-8 -*-

from django import forms
from models import *
from django.db.models.fields import BLANK_CHOICE_DASH


class Search(forms.ModelForm):

    FORMAT_CHOICES = FormatOutil.objects.values_list("nom", "nom")
    FORME_NARRATIVE_CHOICES = FormeNarrative.objects.values_list("nom", "nom")
    PRODUCTEUR_TYPE_CHOICES = ProdType.objects.values_list("nom","nom")
    SUPPORT_DIFFUSION_CHOICES = SupportDiffusion.objects.values_list("nom","nom")
    LANGUE_CHOICES = LangueNarration.objects.exclude(nom="Ne s'applique pas").values_list("nom", "nom")
    MODE_CONSULTATION_CHOICES = ModeConsultation.objects.values_list("nom","nom")
    SONORE_VALEUR_CHOICES = list(SONORE_VALEUR_LIST)
    del SONORE_VALEUR_CHOICES[0]
    EVOCATION_LITTERAIRE_CHOICES = list(EVOCATION_LITTERAIRE_LIST)
    del EVOCATION_LITTERAIRE_CHOICES[0]
    EVOCATION_GRAPHIQUE_CHOICES = EvocationGraphique.objects.exclude(nom="Non").values_list("nom", "nom")
    EVOCATION_PLASTIQUE_CHOICES = EvocationPlastique.objects.exclude(nom="Non").values_list("nom", "nom")
    ORCHESTRATION_CHOICES = Orchestration.objects.exclude(nom="Non").values_list("nom","nom")
    STRUCTURE_CHOICES = Structure.objects.exclude(nom="Non").values_list("nom","nom")
    LANGUAGE_MUSICAL_CHOICES = LanguageMusical.objects.exclude(nom="Non").values_list("nom","nom")
    GENRE_MUSICAL_CHOICES = GenreMusical.objects.exclude(nom="Non").values_list("nom","nom")
    STYLE_MUSICAL_CHOICES = StyleMusical.objects.exclude(nom="Non").values_list("nom","nom")
    EXPERIENCE_MUSICALE_CHOICES = ExperienceMusicale.objects.exclude(nom="Non").values_list("nom","nom")
    CONTEXTE_CHOICES = Contexte.objects.exclude(nom="Non").values_list("nom","nom")
    ROLE_EVOLUTION_CHOICES = RoleEvolution.objects.exclude(nom="Non").values_list("nom","nom")
    EPOQUE_CHOICES = list(EPOQUE_LIST)
    del EPOQUE_CHOICES[11]

    format__nom = forms.ChoiceField(widget = forms.Select, choices=BLANK_CHOICE_DASH + list(FORMAT_CHOICES),
                                          label="Format", required = False)
    forme_narrative__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(FORME_NARRATIVE_CHOICES),
                                             label = "Forme narrative", required = False)
    interactivite = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(INTERACTIVITE_LIST),
                                      label="Interactivité", required=False)
    personnification_service = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(PERSONNIFICATION_LIST),
                                      label="Degré de personnification du service", required=False)
    producteur_type__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(PRODUCTEUR_TYPE_CHOICES),
                                             label="Type de producteur", required=False)
    support_diffusion__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(SUPPORT_DIFFUSION_CHOICES),
                                               label="Support de diffusion", required=False)
    ensemble_thematique = forms.ChoiceField(widget=forms.Select,label="Fait partie d'un ensemble de dispositifs du même type",
                                            choices=BLANK_CHOICE_DASH + list(OUINON), required=False)
    narration_langue__nom = forms.ChoiceField(widget = forms.Select, choices=BLANK_CHOICE_DASH + list(LANGUE_CHOICES),
                                              label = "Langue", required = False)
    mode_consultation__nom = forms.ChoiceField(widget = forms.Select, choices=BLANK_CHOICE_DASH + list(MODE_CONSULTATION_CHOICES),
                                              label = "Mode de consultation", required = False)
    sonore_valeur = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + SONORE_VALEUR_CHOICES,
                                      label="Mise en valeur du sonore", required=False)
    evocation_litteraire = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + EVOCATION_LITTERAIRE_CHOICES,
                                             label = "Évocation littéraire", required=False)
    evocation_graphique__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(EVOCATION_GRAPHIQUE_CHOICES),
                                                 label="Évocation graphique", required=False)
    evocation_plastique__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(EVOCATION_PLASTIQUE_CHOICES),
                                                 label="Évocation plastique", required=False)
    orchestration__nom = forms.ChoiceField(widget=forms.Select,choices=BLANK_CHOICE_DASH + list(ORCHESTRATION_CHOICES),
                                           label="Orchestration", required=False)
    structure__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(STRUCTURE_CHOICES),
                                       label="Structure", required=False)
    language_musical__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(LANGUAGE_MUSICAL_CHOICES),
                                              label="Language musical", required=False)
    genre_musical__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(GENRE_MUSICAL_CHOICES),
                                           label="Genre musical", required=False)
    style_musical__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(STYLE_MUSICAL_CHOICES),
                                           label="Style musical", required=False)
    experience_musicale__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(EXPERIENCE_MUSICALE_CHOICES),
                                                 label="Expérience musicale", required=False)
    contexte__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(CONTEXTE_CHOICES),
                                      label="Contexte", required=False)
    role_evolution__nom = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(ROLE_EVOLUTION_CHOICES),
                                            label="Role de l'évolution du [métier lié à la musique]", required=False)
    epoque = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + EPOQUE_CHOICES,
                               label="Époque (siècle)", required=False)

    # options widgets : Select, SelectMultiple, CheckboxSelectMultiple

    class Meta:
        model = Outil
        fields = [
            #'titre',
            'format__nom',
            'forme_narrative__nom',
            'interactivite',
            'personnification_service',
            'producteur_type__nom',
            'support_diffusion__nom',
            'ensemble_thematique',
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
            'epoque',
        ]