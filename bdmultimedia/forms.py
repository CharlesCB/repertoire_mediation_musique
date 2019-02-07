# -*- coding: utf-8 -*-

from django import forms
from models import *
from django.db.models.fields import BLANK_CHOICE_DASH
from easy_select2 import Select2Multiple, Select2


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
    DISCIPLINE_CHOICES = EvocationAutre.objects.exclude(nom="Aucune").values_list("nom","nom")
    NOTION_CONCEPT_CHOICES = list(OUINONNSP)

    # RÉFÉRENCEMENT
    #referencement = forms.BooleanField(label="Référencement", required = False)
    format__nom = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, choices=list(FORMAT_CHOICES),
                                          label="Format", required = False)
    forme_narrative__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(FORME_NARRATIVE_CHOICES),
                                             label = "Forme narrative", required = False)
    interactivite = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(INTERACTIVITE_LIST),
                                      label="Interactivité", required=False)
    personnification_service = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + list(PERSONNIFICATION_LIST),
                                      label="Degré de personnification du service", required=False)
    producteur_type__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(PRODUCTEUR_TYPE_CHOICES),
                                             label="Type de producteur", required=False)
    support_diffusion__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(SUPPORT_DIFFUSION_CHOICES),
                                               label="Support de diffusion", required=False)
    ensemble_thematique = forms.ChoiceField(widget=forms.Select,label="Fait partie d'un ensemble de dispositifs du même type",
                                            choices=BLANK_CHOICE_DASH + list(OUINON), required=False)

    # DÉCOUVRABILITÉ/ACCESSIBILITÉ
    #decouvrabilite = forms.BooleanField(label="Découvrabilité/Accessibilité", required = False)
    narration_langue__nom = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, choices=list(LANGUE_CHOICES),
                                              label = "Langue", required = False)
    mode_consultation__nom = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, choices=list(MODE_CONSULTATION_CHOICES),
                                              label = "Mode de consultation", required = False)

    sonore_valeur = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + SONORE_VALEUR_CHOICES,
                                      label="Mise en valeur du sonore", required=False)

    # EVOCATION DE LA MUSIQUE EXTTRA_SONORE
    #evocations = forms.BooleanField(label = "Évocation de la musique extra-sonore", required = False)
    evocation_litteraire = forms.ChoiceField(widget=forms.Select, choices=BLANK_CHOICE_DASH + EVOCATION_LITTERAIRE_CHOICES,
                                             label = "Évocation littéraire", required=False)
    evocation_graphique__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(EVOCATION_GRAPHIQUE_CHOICES),
                                                 label="Évocation graphique", required=False)
    evocation_plastique__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(EVOCATION_PLASTIQUE_CHOICES),
                                                 label="Évocation plastique", required=False)
    # ANALYSE MUSICALE
    #analyse_musicale = forms.BooleanField(label="Analyse Musicale", required=False)

    orchestration__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=list(ORCHESTRATION_CHOICES),
                                           label="Orchestration", required=False)
    structure__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(STRUCTURE_CHOICES),
                                       label="Structure", required=False)
    language_musical__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(LANGUAGE_MUSICAL_CHOICES),
                                              label="Language musical", required=False)
    genre_musical__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(GENRE_MUSICAL_CHOICES),
                                           label="Genre musical", required=False)
    style_musical__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(STYLE_MUSICAL_CHOICES),
                                           label="Style musical", required=False)
    # ÉLÉMENTS CONTEXTUELS
    #elements_contextuels = forms.BooleanField(label="Éléments contextuels", required = False)
    experience_musicale__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(EXPERIENCE_MUSICALE_CHOICES),
                                                 label="Expérience musicale", required=False)
    contexte__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(CONTEXTE_CHOICES),
                                      label="Contexte", required=False)
    role_evolution__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(ROLE_EVOLUTION_CHOICES),
                                            label="Rôle de l'évolution du [métier lié à la musique]", required=False)
    epoque__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=EPOQUE_CHOICES,
                               label="Époque (siècle)", required=False)

    # INTERDISCIPLINARITE
    #interdisciplinarite = forms.BooleanField(label='Interdisciplinarité', required=False)
    evocation_autre__nom = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=DISCIPLINE_CHOICES,
                                              label='Discipline(s) évoquée(s)', required=False)
    notion_concepts = forms.ChoiceField(widget=forms.Select, choices = BLANK_CHOICE_DASH + list(OUINONNSP), required=False,
                                       label="Notions communes (luminosité, transparence, vitesse, mouvement)")
    notion_experiences = forms.ChoiceField(widget=forms.Select, choices = BLANK_CHOICE_DASH + list(OUINONNSP), required=False,
                                           label="Expérience (émotions)")
    notion_pratiques = forms.ChoiceField(widget=forms.Select, choices = BLANK_CHOICE_DASH + list(OUINONNSP), required=False,
                                         label="Pratique (processus de création)")

    # options widgets : Select, SelectMultiple, CheckboxSelectMultiple

    class Meta:
        model = Outil
        fields = [
            #'referencement',
            'format__nom',
            'forme_narrative__nom',
            'interactivite',
            'personnification_service',
            'producteur_type__nom',
            'support_diffusion__nom',
            'ensemble_thematique',
            #'decouvrabilite',
            'narration_langue__nom',
            'mode_consultation__nom',
            'sonore_valeur',
            #'evocations',
            'evocation_litteraire',
            'evocation_graphique__nom',
            'evocation_plastique__nom',
            #'analyse_musicale',
            'orchestration__nom',
            'structure__nom',
            'language_musical__nom',
            'genre_musical__nom',
            'style_musical__nom',
            #'elements_contextuels',
            'experience_musicale__nom',
            'contexte__nom',
            'role_evolution__nom',
            'epoque__nom',
        ]


class Create(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Create, self).__init__(*args, **kwargs)
        self.fields['producteur_nom'].help_text = ''
        self.fields['narration_langue'].help_text = ''
        self.fields['sous_titre'].help_text = '<br><br><br>Les sous-titrages automatiques proposés par YouTube n’entrent pas en considération.'

    class Meta:
        model = Outil
        fields = '__all__'
        widgets = {
            #'producteur_type': forms.CheckboxSelectMultiple,
            'producteur_nom': Select2Multiple({'width' : '450px'}),
            # 'support_diffusion': forms.CheckboxSelectMultiple,
            # 'format': forms.CheckboxSelectMultiple,
            # 'forme_narrative': forms.CheckboxSelectMultiple,
            'duree' : forms.TextInput,
            'nb_pages' : forms.TextInput,
            # 'mode_hebergement': forms.CheckboxSelectMultiple,
            # 'mode_consultation': forms.CheckboxSelectMultiple,
             'narration_langue': Select2Multiple({'width' : '450px'}),
             'sous_titre': Select2Multiple({'width' : '450px'}),
            # 'orchestration': forms.CheckboxSelectMultiple,
            # 'structure': Select2Multiple({'width': '450px'}),
            # 'language_musical': Select2Multiple({'width': '450px'}),
            # 'genre_musical': Select2Multiple({'width': '450px'}),
            # 'style_musical': Select2Multiple({'width': '450px'}),
            # 'experience_musicale': Select2Multiple({'width': '450px'}),
            'epoque': forms.CheckboxSelectMultiple(),
            # 'contexte' : forms.CheckboxSelectMultiple,
            # 'role_evolution' : forms.CheckboxSelectMultiple,
            # 'organologie' : forms.CheckboxSelectMultiple,
            # 'sollicitation_musicale': forms.CheckboxSelectMultiple,
            # 'sollicitation_generale' : forms.CheckboxSelectMultiple,
            'temps_mus' : forms.TextInput,
            #
            # 'evocation_graphique' : forms.CheckboxSelectMultiple,
            # 'evocation_plastique' : forms.CheckboxSelectMultiple,
            # 'evocation_autre' : Select2Multiple({'width':'450px'}),
            # 'exemples_notions_interdisciplinaires' : Select2Multiple({'width':'450px'}),
            #
            # 'role_humain_homme' : Select2Multiple({'width':'450px'}),
            # 'role_humain_femme' : Select2Multiple({'width':'450px'}),
            # 'role_humain_neutre' : Select2Multiple({'width':'450px'}),


        }