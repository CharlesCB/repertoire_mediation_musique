from django import forms
from models import *


class Search(forms.ModelForm):
    titre = forms.CharField(label="Recherche par titre")

    class Meta:
        model = Outil
        fields = ['titre']