import django_filters
from .models import Outil

class OutilFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Outil
        fields = ['titre']
