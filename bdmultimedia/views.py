# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from dal import autocomplete
from bdmultimedia.models import *
from django.core.urlresolvers import reverse_lazy
import operator
from multimedia.forms import Create
from django.template import loader
from django.http import HttpResponse
import xlwt

# Create your views here.


class DetailView(generic.DetailView):
    model = Outil
    template_name = 'detail.html'


class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'all_outils'

    def get_queryset(self):
        return Outil.objects.order_by('titre')


class CreateForm(generic.CreateView):
    model = Outil
    template_name = 'create.html'
    form_class = Create
    success_url = '/'
    def get_success_url(self):
        return '/'


class UpdateForm(generic.UpdateView):
    model = Outil
    template_name = 'create.html'
    form_class = Create


class DeleteForm(generic.CreateView):
    model = Outil
    sucess_url = reverse_lazy('/')


class ElemMusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return ElemMus.objects.none()

        qs = ElemMus.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class ExpMusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return ExpMus.objects.none()

        qs = ExpMus.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class PratMusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PratMus.objects.none()

        qs = PratMus.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs

class ElemSocioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return ElemSocio.objects.none()

        qs = ElemSocio.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs

class NotionsInterAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return NotionsInter.objects.none()

        qs = NotionsInter.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


class NotConceptAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return NotConcept.objects.none()

        qs = NotConcept.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs

class NotExpAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return NotExp.objects.none()

        qs = NotExp.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs

class NotPratiqueAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return NotPratique.objects.none()

        qs = NotPratique.objects.all()

        if self.q:
            qs = qs.filter(nom__icontains=self.q)

        return qs


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="donnes_outil_mediation.xls"'

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet('Outils')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.bold = True
    colones = ["Titre", "Url", "Site d'hébergement", "Fait-il partie d'un ensemble thématique?",
               "Nom de l'ensemble thématique", "Producteur", "Nom du producteur",
               "Support de diffusion","Format", "Forme narrative", "Durée", "Nombre de pages",
               "Date de mise en ligne",]

    for col_num in range(len(colones)):
        ws.write(row_num, col_num, colones[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Outil.objects.all().values_list('titre','url','site','ensemble_thematique','ensemble_thematique_nom',
                                           'producteur_type','producteur_nom','support_diffusion','format','forme_narrative',
                                           'duree','nb_pages','mise_en_ligne_date',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,row[col_num],font_style)

    wb.save(response)
    return response