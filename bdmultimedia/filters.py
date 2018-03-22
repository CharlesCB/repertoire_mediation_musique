import django_filters
from .models import Outil
from collections import Iterable
from itertools import chain
from re import search, sub
from django_filters.widgets import BaseCSVWidget, CSVWidget
from django_filters.fields import BaseCSVField
from django_filters.filters import Filter
from dal import autocomplete
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
    titre = MultiValueCharFilter(lookup_expr='icontains')

    class Meta:
        model = Outil
        fields = ['titre']
