from dal import autocomplete
from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from bdmultimedia.models import *
from crispy_forms.helper import FormHelper


class Create(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Create, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Outil
        fields = ('__all__')
        widgets = {
            'liste_materiau': autocomplete.ModelSelect2Multiple(url='elemmus-autocomplete')
        }


