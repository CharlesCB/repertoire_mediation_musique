# -*- coding: utf-8 -*-

import django_filters
from django.db.models.fields import BLANK_CHOICE_DASH
from .models import *
from collections import Iterable
from itertools import chain
from re import search, sub
from django_filters.widgets import BaseCSVWidget, CSVWidget
from django_filters.filters import Filter
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.db.models.constants import LOOKUP_SEP
from django.utils.encoding import force_text


class customCSVWidget(forms.Widget):
    def _isiterable(self, value):
        return isinstance(value, Iterable) and not isinstance(value, str)

    def value_from_datadict(self, data, files, name):
        value = super(customCSVWidget,self).value_from_datadict(data, files, name)

        if value is not None:
            if value == '':  # empty value should parse as an empty list
                return []
            return value.split(' ')
        return None

    def render(self, name, value, attrs=None):
        if not self._isiterable(value):
            value = [value]

        if len(value) <= 1:
            # delegate to main widget (Select, etc...) if not multiple values
            value = value[0] if value else ''
            return super(customCSVWidget,self).render(name, value, attrs)

        # if we have multiple values, we need to force render as a text input
        # (otherwise, the additional values are lost)
        surrogate = forms.TextInput()
        value = [force_text(surrogate._format_value(v)) for v in value]
        value = ' '.join(list(value))

        return surrogate.render(name, value, attrs)


class customCSVField(forms.Field):
    """
    Base field for validating CSV types. Value validation is performed by
    secondary base classes.
    ex::
        class IntegerCSVField(BaseCSVField, filters.IntegerField):
            pass
    """
    base_widget_class = customCSVWidget

    def __init__(self, *args, **kwargs):
        widget = kwargs.get('widget') or self.widget
        kwargs['widget'] = self._get_widget_class(widget)

        super(customCSVField,self).__init__(*args, **kwargs)

    def _get_widget_class(self, widget):
        # passthrough, allows for override
        if isinstance(widget, BaseCSVWidget) or (
                isinstance(widget, type) and
                issubclass(widget, BaseCSVWidget)):
            return widget

        # complain since we are unable to reconstruct widget instances
        assert isinstance(widget, type), \
            "'%s.widget' must be a widget class, not %s." \
            % (self.__class__.__name__, repr(widget))

        bases = (self.base_widget_class, widget, )
        return type(str('CSV%s' % widget.__name__), bases, {})

    def clean(self, value):
        if value is None:
            return None
        return [super(customCSVField, self).clean(v) for v in value]


class customCSVFilter(Filter):
    """
    Base class for CSV type filters, such as IN and RANGE.
    """
    base_field_class = customCSVField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('help_text', _('Multiple values may be separated by commas.'))
        super(customCSVFilter,self).__init__(*args, **kwargs)

        class ConcreteCSVField(self.base_field_class, self.field_class):
            pass
        ConcreteCSVField.__name__ = self._field_class_name(
            self.field_class, self.lookup_expr
        )

        self.field_class = ConcreteCSVField

    @classmethod
    def _field_class_name(cls, field_class, lookup_expr):
        """
        Generate a suitable class name for the concrete field class. This is not
        completely reliable, as not all field class names are of the format
        <Type>Field.
        ex::
            BaseCSVFilter._field_class_name(DateTimeField, 'year__in')
            returns 'DateTimeYearInField'
        """
        # DateTimeField => DateTime
        type_name = field_class.__name__
        if type_name.endswith('Field'):
            type_name = type_name[:-5]

        # year__in => YearIn
        parts = lookup_expr.split(LOOKUP_SEP)
        expression_name = ''.join(p.capitalize() for p in parts)

        # DateTimeYearInField
        return str('%s%sField' % (type_name, expression_name))


class MultiValueCharFilter(customCSVFilter, django_filters.CharFilter):
    def filter(self, qs, value):
        # value is either a list or an 'empty' value
        values = value or []

        for value in values:
            qs = super(MultiValueCharFilter, self).filter(qs, value)

        return qs


class OutilFilter(django_filters.FilterSet):

    ##fields = list([f.name for f in Outil._meta.get_fields()])
    ##del fields[0]

    noms = []
    for f in Outil._meta.get_fields():
        if f.__class__.__name__ == "ManyToManyField":
            noms.append(f.name + "__nom")
        elif f.__class__.__name__ != "AutoField":
            noms.append(f.name)



    FORMAT_CHOICES = BLANK_CHOICE_DASH + list(FormatOutil.objects.all().values_list("nom","nom"))

    FORME_NARRATIVE_CHOICES = BLANK_CHOICE_DASH + list(FormeNarrative.objects.values_list("nom","nom"))

    PRODUCTEUR_TYPE_CHOICES = BLANK_CHOICE_DASH + list(ProdType.objects.values_list("nom","nom"))

    SUPPORT_DIFFUSION_CHOICES = BLANK_CHOICE_DASH + list(SupportDiffusion.objects.values_list("nom","nom"))

    LANGUE_CHOICES = BLANK_CHOICE_DASH + list(LangueNarration.objects.exclude(nom = "Ne s'applique pas").values_list("nom","nom"))

    MODE_CONSULTATION_CHOICES = BLANK_CHOICE_DASH + list(ModeConsultation.objects.values_list("nom","nom"))

    SONORE_VALEUR_CHOICES = list(SONORE_VALEUR_LIST)
    del SONORE_VALEUR_CHOICES[0]

    EVOCATION_LITTERAIRE_CHOICES =  list(EVOCATION_LITTERAIRE_LIST)
    del EVOCATION_LITTERAIRE_CHOICES[0]

    EVOCATION_GRAPHIQUE_CHOICES = BLANK_CHOICE_DASH + list(EvocationGraphique.objects.exclude(nom="Non").values_list("nom","nom"))

    EVOCATION_PLASTIQUE_CHOICES = BLANK_CHOICE_DASH + list(EvocationPlastique.objects.exclude(nom="Non").values_list("nom", "nom"))

    ORCHESTRATION_CHOICES = BLANK_CHOICE_DASH + list(Orchestration.objects.exclude(nom="Non").values_list("nom","nom"))

    STRUCTURE_CHOICES = BLANK_CHOICE_DASH + list(Structure.objects.exclude(nom="Non").values_list("nom", "nom"))

    LANGUAGE_MUSICAL_CHOICES = BLANK_CHOICE_DASH + list(LanguageMusical.objects.exclude(nom="Non").values_list("nom", "nom"))

    GENRE_MUSICAL_CHOICES = BLANK_CHOICE_DASH + list(GenreMusical.objects.exclude(nom="Non").values_list("nom", "nom"))

    STYLE_MUSICAL_CHOICES = BLANK_CHOICE_DASH + list(StyleMusical.objects.exclude(nom="Non").values_list("nom", "nom"))

    EXPERIENCE_MUSICALE_CHOICES = BLANK_CHOICE_DASH + list(ExperienceMusicale.objects.exclude(nom="Non").values_list("nom", "nom"))

    CONTEXTE_CHOICES = BLANK_CHOICE_DASH + list(Contexte.objects.exclude(nom="Non").values_list("nom","nom"))

    ROLE_EVOLUTION_CHOICES = BLANK_CHOICE_DASH + list(RoleEvolution.objects.exclude(nom="Non").values_list("nom", "nom"))

    EPOQUE_CHOICES = list(EPOQUE_LIST)
    del EPOQUE_CHOICES[11]

    # titre = MultiValueCharFilter(lookup_expr='icontains')

    format__nom = django_filters.ChoiceFilter(choices=FORMAT_CHOICES, lookup_expr='iexact')
    forme_narrative__nom = django_filters.ChoiceFilter(choices=FORME_NARRATIVE_CHOICES,
                                                       lookup_expr="iexact")
    interactivite = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + list(INTERACTIVITE_LIST),
                                                lookup_expr='iexact')
    personnification_service = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + list(PERSONNIFICATION_LIST),
                                                           lookup_expr="iexact")
    producteur_type__nom = django_filters.ChoiceFilter(choices=PRODUCTEUR_TYPE_CHOICES,
                                                       lookup_expr='iexact')
    support_diffusion__nom = django_filters.ChoiceFilter(choices=SUPPORT_DIFFUSION_CHOICES,
                                                         lookup_expr='iexact')
    ensemble_thematique = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + list(OUINON),
                                                      lookup_expr="exact")
    narration_langue__nom = django_filters.ChoiceFilter(choices=LANGUE_CHOICES, lookup_expr='iexact')
    mode_consultation__nom = django_filters.ChoiceFilter(choices=MODE_CONSULTATION_CHOICES,
                                                         lookup_expr='iexact')
    sonore_valeur = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + SONORE_VALEUR_CHOICES,
                                                lookup_expr="exact")
    evocation_litteraire = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + EVOCATION_LITTERAIRE_CHOICES,
                                                       lookup_expr="iexact")
    evocation_graphique__nom = django_filters.ChoiceFilter(choices=EVOCATION_GRAPHIQUE_CHOICES,
                                                           lookup_expr="iexact")
    evocation_plastique__nom = django_filters.ChoiceFilter(choices=EVOCATION_PLASTIQUE_CHOICES,
                                                           lookup_expr="iexact")
    #ANALYSE MUSICALE
    orchestration__nom = django_filters.ChoiceFilter(choices=ORCHESTRATION_CHOICES, lookup_expr = "iexact")
    structure__nom = django_filters.ChoiceFilter(choices=STRUCTURE_CHOICES, lookup_expr="iexact")
    language_musical__nom = django_filters.ChoiceFilter(choices=LANGUAGE_MUSICAL_CHOICES, lookup_expr="iexact")
    genre_musical__nom = django_filters.ChoiceFilter(choices=GENRE_MUSICAL_CHOICES, lookup_expr="iexact")
    style_musical__nom = django_filters.ChoiceFilter(choices=STYLE_MUSICAL_CHOICES, lookup_expr="iexact")

    #ÉLÉMENTS CONTEXTUELS
    experience_musicale__nom = django_filters.ChoiceFilter(choices=EXPERIENCE_MUSICALE_CHOICES, lookup_expr="iexact")
    contexte__nom = django_filters.ChoiceFilter(choices=CONTEXTE_CHOICES, lookup_expr="iexact")
    role_evolution__nom = django_filters.ChoiceFilter(choices=ROLE_EVOLUTION_CHOICES, lookup_expr="iexact")
    epoque = django_filters.ChoiceFilter(choices=BLANK_CHOICE_DASH + EPOQUE_CHOICES, lookup_expr="icontains")

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

