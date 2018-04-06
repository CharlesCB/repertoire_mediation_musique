# -*- coding: utf-8 -*-

from django import forms
from models import *
from django.db.models.fields import BLANK_CHOICE_DASH


class Search(forms.ModelForm):
    SUPPORT_CHOICES = SupportDiffusion.objects.all().values_list("nom", "nom")
    MODE_HEBERGEMENT_CHOICES = ModeHebergement.objects.all().values_list("nom","nom")
    FORMAT_CHOICES = FormatOutil.objects.all().values_list("nom", "nom")

    titre = forms.CharField(label="Titre", required = False)
    format__nom = forms.ChoiceField(widget = forms.Select, choices=BLANK_CHOICE_DASH + list(FORMAT_CHOICES),
                                          label="Format", required = False)
    mode_hebergement__nom = forms.ChoiceField(widget = forms.Select, choices=BLANK_CHOICE_DASH + list(MODE_HEBERGEMENT_CHOICES),
                                              label = "Mode d'hébergement", required = False)
    #support_diffusion__nom = forms.ChoiceField(widget=forms.Select,choices=BLANK_CHOICE_DASH + list(SUPPORT_CHOICES),
    #                                           label="Support de diffusion", required = False)

    class Meta:
        model = Outil
        fields = ['titre', 'format__nom', 'mode_hebergement__nom' ]