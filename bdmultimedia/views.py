# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from dal import autocomplete
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bdmultimedia.models import *
from django.core.urlresolvers import reverse_lazy
import operator
from multimedia.forms import Create
from django.template import loader
from django.http import HttpResponse
import xlwt
from .filters import OutilFilter
from forms import Search

# Create your views here.



class DetailView(generic.DetailView):
    model = Outil
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['tout'] = Outil.objects.order_by('titre')
        return context


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


class OutilList(generic.View):
    def get(self, request):

        data = OutilFilter(self.request.GET, queryset = Outil.objects.all())
        data_total = data.qs.count()
        all_main_registers = OutilFilter(self.request.GET, queryset=Outil.objects.all().order_by('titre'))


        paginator = Paginator(data.qs, 25)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        return render(request, 'results.html', {'items': items, 'all': all_main_registers, 'form': all_main_registers.form, 'data_total' : data_total})


class SearchForm(generic.View):
    def get(self, request):
        search_form = Search()
        return render(request, 'search.html', {'form': search_form})

    def post(self, request):
        pass

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
