# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bdmultimedia.models import *
from django.core.urlresolvers import reverse_lazy
from multimedia.forms import Create
from django.http import HttpResponse
import xlwt
from .filters import OutilFilter
from forms import Search
import csv, tempfile, os
import datetime

# Create your views here.


class DetailView(generic.DetailView):
    model = Outil
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['tout'] = Outil.objects.order_by('titre')
        context['liste'] = Outil.objects.all().values_list()

        return context


class OutilDelete(generic.DeleteView):
    model = Outil
    success_url = reverse_lazy('home') # This is where this view will
                                            # redirect the user
    template_name = 'delete_outil.html'


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


class ListDetailView(generic.DetailView):
    model = Outil
    template_name = 'list_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        #context['tout'] = OutilFilter(self.request.GET, queryset=Outil.objects.all()).qs

        return context


class OutilList(generic.View):
    def get(self, request):

        data = OutilFilter(self.request.GET, queryset = Outil.objects.all().order_by('duree').reverse())
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
    if request.user.is_authenticated():
        response = HttpResponse(content_type='application/ms-excel')
        aujourdui = datetime.datetime.now().strftime('%d/%m/%Y')
        nom = "[" + aujourdui + "] Catalogue raisonné dispositifs numérique.xls"
        response['Content-Disposition'] = 'attachment; filename=%s' % nom

        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet('Outils')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.bold = True
        date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

        colones = ["R.1 Titre", "R.2 Url", "R.3 Site d'hébergement", "R.3.1 Fait-il partie d'un ensemble thématique?",
                   "R.3.2 Nom de l'ensemble thématique", "R.4 Producteur", "R.5 Nom du producteur",
                   "R.6 Support de diffusion","R.7 Format", "R.8 Forme narrative", "R.9 Durée", "R.10 Nombre de pages",
                   "R.11 Date de mise en ligne", "R.12 Date du dépouillement", "R.13 Que permet l'interface",
                   "R.14 Personnification du service","R.15 Possibilité de laisser des commentaires", "R.16 Nombre de commentaires",
                   "S.17 Premier Onglet","S.17.1 Autre - Premier Onglet","S.18 Deuxième Onglet","S.18.1 Autre - Deuxième Onglet",
                   "S.19 Troisième Onglet","S19.1 Autre Troisième Onglet","S.20 Mode d'hébergement","S.21 Mode de consultation",
                   "S.22 langue de la narration","S.23 Sous-titrages", "S.24.1 Accessible aux malentendants","S.24.2 Accessible aux malcoyants",
                   "M.25 Matériau musical (parle-t-on)","M.25.1 Orchestration (parle-t-on)",
                   "M.25.2 Structure (parle-t-on)", "M.25.3 language musical (parle-t-on)","M.25.4 genre musica (parle-t-on)l", "M.25.5 style musical (parle-t-on)",
                   "M.26 Expérience musicale (parle-t-on)", "M.27 Éléments sociocultutrels et historique (parle-t-on)", "M.27.1 Époque",
                   "M.28 Contexte de composition, création, interprétation", "U.28 Rôle de l'évolution",
                   "U.28 Sollicitation musicale", "U.29 Sollicifation générale", "PM.30 temps de musique", "PM.31 temps de parole", "PM.32 temps musique et parole",
                   "PM.33 mise en valeur du sonore", "EM.34 évocation graphique", "EM.35 évocation plastique", "EM.36 évocation litteraire",
                   "EM.37 autre discipline évoquée", "I.38 notions communes", "I.38 expérience", "I.38 pratique", 
                   "I.39 exemples de notions évoquées de façon interdisciplinaires", "STÉ.39.1 nombre total d'humains", "STÉ.39.1 nombre d'hommes",
                   "STÉ.39.1 nombre de femmes","STÉ.39.1 Nombre d'humains au genre indéterminé", "Sté.39.2 Rôle des femmes", "Sté.39.3 Rôle des hommes",
                   "Sté.39.4 Rôle des indeterminés","Sté.40.1 Nombre de personnages animés total","Sté.40.1 Nombre de personnages animés hommes",
                   "Sté.40.1 Nombre de personnages animés femmes", "Sté.40.1 Nombre de personnages animés au genre indéterminé",
                   "Sté.40.3 Rôle des personnages animés féminins", "Sté.40.2 Rôle des personnages animés masculins", "Sté.40.4 Rôle des personnages animés indéterminés",
                   "Sté.41.1 Nombre d'animaux total", "Sté.41.1 Nombre de mâles", "Sté.41.1 Nombre de femelles", "Sté.41.1 Nombre d'animaux au genre indéterminé",
                   "Sté.41.3 Rôle des animaux femelles", "Sté.41.2 Rôle des animaux mâles", "Sté.41.4 Rôle des animaux indéterminés",
                   "Sté.42.1 Nombre d'instruments animés total", "Sté.42.1 Nombre d'instruments animés masculins", "Sté.42.1 Nombre d'instruments animés féminins",
                   "Sté.42.1 Nombre d'instruments animés au genre indéterminé", "Sté.42.3 Rôle des instruments anthropomorphes féminins",
                   "Sté.42.2 Rôle des instruments anthropomorphes masculins", "Sté.42.4 Rôle des instruments anthropomorphes neutres",
                   ]

        for col_num in range(len(colones)):
            ws.write(row_num, col_num, colones[col_num], font_style)

        loftUn = list(Outil.objects.all().values_list('titre','url','site','ensemble_thematique','ensemble_thematique_nom', 'producteur_type__nom'))
        loflUn = [list(elem) for elem in loftUn]
        loftDeux = list(Outil.objects.all().values_list('titre','producteur_nom','support_diffusion__nom'))
        loflDeux = [list(elem) for elem in loftDeux]
        loftTrois = list(Outil.objects.all().values_list('titre','format__nom'))
        loflTrois = [list(elem) for elem in loftTrois]
        loftQuatre = list(Outil.objects.all().values_list('titre','forme_narrative__nom','duree','nb_pages','mise_en_ligne_date','depouillement_date','interface',
                                                          'personnification_service','commentaire_possible','commentaire_nombre','premier_onglet', 'prem_onglet_autre',
                                                          'deuxieme_onglet', 'deux_onglet_autre', 'troisieme_onglet', 'trois_onglet_autre'))
        loflQuatre = [list(elem) for elem in loftQuatre]
        loftCinq = list(Outil.objects.all().values_list('titre','mode_hebergement__nom'))
        loflCinq = [list(elem) for elem in loftCinq]
        loftSix = list(Outil.objects.all().values_list('titre','mode_consultation__nom'))
        loflSix = [list(elem) for elem in loftSix]
        loftSept = list(Outil.objects.all().values_list('titre','narration_langue__nom'))
        loflSept = [list(elem) for elem in loftSept]
        loftHuit = list(Outil.objects.all().values_list('titre','sous_titre__nom', 'malentendants', 'malvoyants', 'materiau_musical'))
        loflHuit = [list(elem) for elem in loftHuit]
        loftNeuf = list(Outil.objects.all().values_list('titre','orchestration__nom'))
        loflNeuf = [list(elem) for elem in loftNeuf]
        loftDix = list(Outil.objects.all().values_list('titre','structure__nom'))
        loflDix = [list(elem) for elem in loftDix]
        loftOnze = list(Outil.objects.all().values_list('titre','language_musical__nom'))
        loflOnze = [list(elem) for elem in loftOnze]
        loftDouze = list(Outil.objects.all().values_list('titre','genre_musical__nom'))
        loflDouze = [list(elem) for elem in loftDouze]
        loftTreize = list(Outil.objects.all().values_list('titre','style_musical__nom'))
        loflTreize = [list(elem) for elem in loftTreize]
        loftQuatorze = list(Outil.objects.all().values_list('titre','experience_musicale__nom', 'elements_socioculturels', 'epoque'))
        loflQuatorze = [list(elem) for elem in loftQuatorze]
        loftQuinze = list(Outil.objects.all().values_list('titre','contexte__nom'))
        loflQuinze = [list(elem) for elem in loftQuinze]
        loftSeize = list(Outil.objects.all().values_list('titre','role_evolution__nom'))
        loflSeize = [list(elem) for elem in loftSeize]
        loftDixSept = list(Outil.objects.all().values_list('titre','sollicitation_musicale__nom'))
        loflDixSept = [list(elem) for elem in loftDixSept]
        loftDixHuit = list(Outil.objects.all().values_list('titre','sollicitation_generale__nom', 'temps_mus', 'temps_par', 'temps_mus_par', 'sonore_valeur'))
        loflDixHuit = [list(elem) for elem in loftDixHuit]
        loftDixNeuf = list(Outil.objects.all().values_list('titre', 'evocation_graphique__nom'))
        loflDixNeuf = [list(elem) for elem in loftDixNeuf]
        loftVingt = list(Outil.objects.all().values_list('titre', 'evocation_plastique__nom', 'evocation_litteraire'))
        loflVingt = [list(elem) for elem in loftVingt]
        loftVingtEtUn = list(Outil.objects.all().values_list('titre', 'evocation_autre__nom', 'notion_concepts', 'notion_experiences', 'notion_pratiques'))
        loflVingtEtUn = [list(elem) for elem in loftVingtEtUn]
        loftVingtDeux = list(Outil.objects.all().values_list('titre', 'exemples_notions_interdisciplinaires__nom', 'nb_humains_total', 'nb_hommes', 'nb_femmes',
                                                             'nb_humains_indetermines'))
        loflVingtDeux = [list(elem) for elem in loftVingtDeux]
        loftVingtTrois = list(Outil.objects.all().values_list('titre', 'role_humain_femme__nom'))
        loflVingtTrois = [list(elem) for elem in loftVingtTrois]
        loftVingtQuatre = list(Outil.objects.all().values_list('titre', 'role_humain_homme__nom'))
        loflVingtQuatre = [list(elem) for elem in loftVingtQuatre]
        loftVingtCinq = list(Outil.objects.all().values_list('titre', 'role_humain_neutre__nom', 'nb_pers_anime_total', 'nb_pers_anime_hommes',
                                                             'nb_pers_anime_femmes', 'nb_pers_anime_indetermines'))
        loflVingtCinq = [list(elem) for elem in loftVingtCinq]
        loftVingtSix = list(Outil.objects.all().values_list('titre', 'role_pers_anime_femme__nom'))
        loflVingtSix = [list(elem) for elem in loftVingtSix]
        loftVingtSept = list(Outil.objects.all().values_list('titre', 'role_pers_anime_homme__nom'))
        loflVingtSept = [list(elem) for elem in loftVingtSept]
        loftVingtHuit = list(Outil.objects.all().values_list('titre', 'role_pers_anime_neutre__nom', 'nb_animaux_total', 'nb_males', 'nb_femelles',
                                                             'nb_animaux_indetermines'))
        loflVingtHuit = [list(elem) for elem in loftVingtHuit]
        loftVingtNeuf = list(Outil.objects.all().values_list('titre', 'role_animaux_femme__nom'))
        loflVingtNeuf = [list(elem) for elem in loftVingtNeuf]
        loftTrente = list(Outil.objects.all().values_list('titre', 'role_animaux_homme__nom'))
        loflTrente = [list(elem) for elem in loftTrente]
        loftTrenteEtUn = list(Outil.objects.all().values_list('titre','role_animaux_neutre__nom', 'nb_instr_anime_total', 'nb_instr_anime_hommes',
                                                              'nb_instr_anime_femmes', 'nb_instr_anime_indetermines'))
        loflTrenteEtUn = [list(elem) for elem in loftTrenteEtUn]
        loftTrenteDeux = list(Outil.objects.all().values_list('titre', 'role_instr_anime_femme__nom'))
        loflTrenteDeux = [list(elem) for elem in loftTrenteDeux]
        loftTrenteTrois = list(Outil.objects.all().values_list('titre', 'role_instr_anime_homme__nom'))
        loflTrenteTrois = [list(elem) for elem in loftTrenteTrois]
        loftTrenteQuatre = list(Outil.objects.all().values_list('titre', 'role_instr_anime_neutre__nom'))
        loflTrenteQuatre = [list(elem) for elem in loftTrenteQuatre]
        
        total = Outil.objects.all().count()

        loflFin = [None] * total

        # un
        for i in range(4):
            for item in loflUn:
                if loflUn.index(item) != len(loflUn) - 1:
                    prem = loflUn[loflUn.index(item)]
                    deux = loflUn[loflUn.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[5] not in deux[5]:
                            prem[5] += ", "
                            prem[5] += deux[5]
                            loflUn[loflUn.index(item)] = prem
                            del loflUn[loflUn.index(item) + 1]

        # deux
        for i in range(3):
            for item in loflDeux:
                if loflDeux.index(item) != len(loflDeux) - 1:
                    prem = loflDeux[loflDeux.index(item)]
                    deux = loflDeux[loflDeux.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[2] not in deux[2]:
                            prem[2] += ", "
                            prem[2] += deux[2]
                            loflDeux[loflDeux.index(item)] = prem
                            del loflDeux[loflDeux.index(item) + 1]

        # trois
        for i in range(3):
            for item in loflTrois:
                if loflTrois.index(item) != len(loflTrois) - 1:
                    prem = loflTrois[loflTrois.index(item)]
                    Trois = loflTrois[loflTrois.index(item) + 1]
                    if prem[0] == Trois[0]:
                        if prem[1] not in Trois[1]:
                            prem[1] += ", "
                            prem[1] += Trois[1]
                            loflTrois[loflTrois.index(item)] = prem
                            del loflTrois[loflTrois.index(item) + 1]

        # quatre
        for i in range(3):
            for item in loflQuatre:
                if loflQuatre.index(item) != len(loflQuatre) - 1:
                    prem = loflQuatre[loflQuatre.index(item)]
                    Quatre = loflQuatre[loflQuatre.index(item) + 1]
                    if prem[0] == Quatre[0]:
                        if prem[1] not in Quatre[1]:
                            prem[1] += ", "
                            prem[1] += Quatre[1]
                            loflQuatre[loflQuatre.index(item)] = prem
                            del loflQuatre[loflQuatre.index(item) + 1]

        # cinq
        for i in range(3):
            for item in loflCinq:
                if loflCinq.index(item) != len(loflCinq) - 1:
                    prem = loflCinq[loflCinq.index(item)]
                    Cinq = loflCinq[loflCinq.index(item) + 1]
                    if prem[0] == Cinq[0]:
                        if prem[1] not in Cinq[1]:
                            prem[1] += ", "
                            prem[1] += Cinq[1]
                            loflCinq[loflCinq.index(item)] = prem
                            del loflCinq[loflCinq.index(item) + 1]

        # six
        for i in range(3):
            for item in loflSix:
                if loflSix.index(item) != len(loflSix) - 1:
                    prem = loflSix[loflSix.index(item)]
                    Six = loflSix[loflSix.index(item) + 1]
                    if prem[0] == Six[0]:
                        if prem[1] not in Six[1]:
                            prem[1] += ", "
                            prem[1] += Six[1]
                            loflSix[loflSix.index(item)] = prem
                            del loflSix[loflSix.index(item) + 1]

        # sept
        for i in range(3):
            for item in loflSept:
                if loflSept.index(item) != len(loflSept) - 1:
                    prem = loflSept[loflSept.index(item)]
                    Sept = loflSept[loflSept.index(item) + 1]
                    if prem[0] == Sept[0]:
                        if prem[1] not in Sept[1]:
                            prem[1] += ", "
                            prem[1] += Sept[1]
                            loflSept[loflSept.index(item)] = prem
                            del loflSept[loflSept.index(item) + 1]

        # huit
        for i in range(3):
            for item in loflHuit:
                if loflHuit.index(item) != len(loflHuit) - 1:
                    prem = loflHuit[loflHuit.index(item)]
                    Huit = loflHuit[loflHuit.index(item) + 1]
                    if prem[0] == Huit[0]:
                        if prem[1] not in Huit[1]:
                            prem[1] += ", "
                            prem[1] += Huit[1]
                            loflHuit[loflHuit.index(item)] = prem
                            del loflHuit[loflHuit.index(item) + 1]

        # neuf
        for i in range(3):
            for item in loflNeuf:
                if loflNeuf.index(item) != len(loflNeuf) - 1:
                    prem = loflNeuf[loflNeuf.index(item)]
                    Neuf = loflNeuf[loflNeuf.index(item) + 1]
                    if prem[0] == Neuf[0]:
                        if prem[1] not in Neuf[1]:
                            prem[1] += ", "
                            prem[1] += Neuf[1]
                            loflNeuf[loflNeuf.index(item)] = prem
                            del loflNeuf[loflNeuf.index(item) + 1]

        # dix
        for i in range(3):
            for item in loflDix:
                if loflDix.index(item) != len(loflDix) - 1:
                    prem = loflDix[loflDix.index(item)]
                    Dix = loflDix[loflDix.index(item) + 1]
                    if prem[0] == Dix[0]:
                        if prem[1] not in Dix[1]:
                            prem[1] += ", "
                            prem[1] += Dix[1]
                            loflDix[loflDix.index(item)] = prem
                            del loflDix[loflDix.index(item) + 1]

        # onze
        for i in range(3):
            for item in loflOnze:
                if loflOnze.index(item) != len(loflOnze) - 1:
                    prem = loflOnze[loflOnze.index(item)]
                    Onze = loflOnze[loflOnze.index(item) + 1]
                    if prem[0] == Onze[0]:
                        if prem[1] not in Onze[1]:
                            prem[1] += ", "
                            prem[1] += Onze[1]
                            loflOnze[loflOnze.index(item)] = prem
                            del loflOnze[loflOnze.index(item) + 1]
                            
        # douze
        for i in range(3):
            for item in loflDouze:
                if loflDouze.index(item) != len(loflDouze) - 1:
                    prem = loflDouze[loflDouze.index(item)]
                    Douze = loflDouze[loflDouze.index(item) + 1]
                    if prem[0] == Douze[0]:
                        if prem[1] not in Douze[1]:
                            prem[1] += ", "
                            prem[1] += Douze[1]
                            loflDouze[loflDouze.index(item)] = prem
                            del loflDouze[loflDouze.index(item) + 1]
                            
        # treize
        for i in range(3):
            for item in loflTreize:
                if loflTreize.index(item) != len(loflTreize) - 1:
                    prem = loflTreize[loflTreize.index(item)]
                    Treize = loflTreize[loflTreize.index(item) + 1]
                    if prem[0] == Treize[0]:
                        if prem[1] not in Treize[1]:
                            prem[1] += ", "
                            prem[1] += Treize[1]
                            loflTreize[loflTreize.index(item)] = prem
                            del loflTreize[loflTreize.index(item) + 1]
        
        # quatorze
        for i in range(3):
            for item in loflQuatorze:
                if loflQuatorze.index(item) != len(loflQuatorze) - 1:
                    prem = loflQuatorze[loflQuatorze.index(item)]
                    Quatorze = loflQuatorze[loflQuatorze.index(item) + 1]
                    if prem[0] == Quatorze[0]:
                        if prem[1] not in Quatorze[1]:
                            prem[1] += ", "
                            prem[1] += Quatorze[1]
                            loflQuatorze[loflQuatorze.index(item)] = prem
                            del loflQuatorze[loflQuatorze.index(item) + 1]

        # quinze
        for i in range(3):
            for item in loflQuinze:
                if loflQuinze.index(item) != len(loflQuinze) - 1:
                    prem = loflQuinze[loflQuinze.index(item)]
                    Quinze = loflQuinze[loflQuinze.index(item) + 1]
                    if prem[0] == Quinze[0]:
                        if prem[1] not in Quinze[1]:
                            prem[1] += ", "
                            prem[1] += Quinze[1]
                            loflQuinze[loflQuinze.index(item)] = prem
                            del loflQuinze[loflQuinze.index(item) + 1]
        
        # seize
        for i in range(3):
            for item in loflSeize:
                if loflSeize.index(item) != len(loflSeize) - 1:
                    prem = loflSeize[loflSeize.index(item)]
                    Seize = loflSeize[loflSeize.index(item) + 1]
                    if prem[0] == Seize[0]:
                        if prem[1] not in Seize[1]:
                            prem[1] += ", "
                            prem[1] += Seize[1]
                            loflSeize[loflSeize.index(item)] = prem
                            del loflSeize[loflSeize.index(item) + 1]
        
        # dix-sept
        for i in range(3):
            for item in loflDixSept:
                if loflDixSept.index(item) != len(loflDixSept) - 1:
                    prem = loflDixSept[loflDixSept.index(item)]
                    DixSept = loflDixSept[loflDixSept.index(item) + 1]
                    if prem[0] == DixSept[0]:
                        if prem[1] not in DixSept[1]:
                            prem[1] += ", "
                            prem[1] += DixSept[1]
                            loflDixSept[loflDixSept.index(item)] = prem
                            del loflDixSept[loflDixSept.index(item) + 1]
                            
        # dix-huit
        for i in range(3):
            for item in loflDixHuit:
                if loflDixHuit.index(item) != len(loflDixHuit) - 1:
                    prem = loflDixHuit[loflDixHuit.index(item)]
                    DixHuit = loflDixHuit[loflDixHuit.index(item) + 1]
                    if prem[0] == DixHuit[0]:
                        if prem[1] not in DixHuit[1]:
                            prem[1] += ", "
                            prem[1] += DixHuit[1]
                            loflDixHuit[loflDixHuit.index(item)] = prem
                            del loflDixHuit[loflDixHuit.index(item) + 1]
        
        # dix-Neuf
        for i in range(3):
            for item in loflDixNeuf:
                if loflDixNeuf.index(item) != len(loflDixNeuf) - 1:
                    prem = loflDixNeuf[loflDixNeuf.index(item)]
                    DixNeuf = loflDixNeuf[loflDixNeuf.index(item) + 1]
                    if prem[0] == DixNeuf[0]:
                        if prem[1] not in DixNeuf[1]:
                            prem[1] += ", "
                            prem[1] += DixNeuf[1]
                            loflDixNeuf[loflDixNeuf.index(item)] = prem
                            del loflDixNeuf[loflDixNeuf.index(item) + 1]

        # vingt
        for i in range(3):
            for item in loflVingt:
                if loflVingt.index(item) != len(loflVingt) - 1:
                    prem = loflVingt[loflVingt.index(item)]
                    Vingt = loflVingt[loflVingt.index(item) + 1]
                    if prem[0] == Vingt[0]:
                        if prem[1] not in Vingt[1]:
                            prem[1] += ", "
                            prem[1] += Vingt[1]
                            loflVingt[loflVingt.index(item)] = prem
                            del loflVingt[loflVingt.index(item) + 1]
                            
        # vingt-et-un
        for i in range(3):
            for item in loflVingtEtUn:
                if loflVingtEtUn.index(item) != len(loflVingtEtUn) - 1:
                    prem = loflVingtEtUn[loflVingtEtUn.index(item)]
                    VingtEtUn = loflVingtEtUn[loflVingtEtUn.index(item) + 1]
                    if prem[0] == VingtEtUn[0]:
                        if prem[1] not in VingtEtUn[1]:
                            prem[1] += ", "
                            prem[1] += VingtEtUn[1]
                            loflVingtEtUn[loflVingtEtUn.index(item)] = prem
                            del loflVingtEtUn[loflVingtEtUn.index(item) + 1]
                            
        # vingt-deux
        for i in range(3):
            for item in loflVingtDeux:
                if loflVingtDeux.index(item) != len(loflVingtDeux) - 1:
                    prem = loflVingtDeux[loflVingtDeux.index(item)]
                    VingtDeux = loflVingtDeux[loflVingtDeux.index(item) + 1]
                    if prem[0] == VingtDeux[0]:
                        if prem[1] not in VingtDeux[1]:
                            prem[1] += ", "
                            prem[1] += VingtDeux[1]
                            loflVingtDeux[loflVingtDeux.index(item)] = prem
                            del loflVingtDeux[loflVingtDeux.index(item) + 1]
                            
        # vingt-trois
        for i in range(3):
            for item in loflVingtTrois:
                if loflVingtTrois.index(item) != len(loflVingtTrois) - 1:
                    prem = loflVingtTrois[loflVingtTrois.index(item)]
                    VingtTrois = loflVingtTrois[loflVingtTrois.index(item) + 1]
                    if prem[0] == VingtTrois[0]:
                        if prem[1] not in VingtTrois[1]:
                            prem[1] += ", "
                            prem[1] += VingtTrois[1]
                            loflVingtTrois[loflVingtTrois.index(item)] = prem
                            del loflVingtTrois[loflVingtTrois.index(item) + 1]
                            
        # vingt-quatre
        for i in range(3):
            for item in loflVingtQuatre:
                if loflVingtQuatre.index(item) != len(loflVingtQuatre) - 1:
                    prem = loflVingtQuatre[loflVingtQuatre.index(item)]
                    VingtQuatre = loflVingtQuatre[loflVingtQuatre.index(item) + 1]
                    if prem[0] == VingtQuatre[0]:
                        if prem[1] not in VingtQuatre[1]:
                            prem[1] += ", "
                            prem[1] += VingtQuatre[1]
                            loflVingtQuatre[loflVingtQuatre.index(item)] = prem
                            del loflVingtQuatre[loflVingtQuatre.index(item) + 1]
                            
        # vingt-cinq
        for i in range(3):
            for item in loflVingtCinq:
                if loflVingtCinq.index(item) != len(loflVingtCinq) - 1:
                    prem = loflVingtCinq[loflVingtCinq.index(item)]
                    VingtCinq = loflVingtCinq[loflVingtCinq.index(item) + 1]
                    if prem[0] == VingtCinq[0]:
                        if prem[1] not in VingtCinq[1]:
                            prem[1] += ", "
                            prem[1] += VingtCinq[1]
                            loflVingtCinq[loflVingtCinq.index(item)] = prem
                            del loflVingtCinq[loflVingtCinq.index(item) + 1]

        # vingt-six
        for i in range(3):
            for item in loflVingtSix:
                if loflVingtSix.index(item) != len(loflVingtSix) - 1:
                    prem = loflVingtSix[loflVingtSix.index(item)]
                    VingtSix = loflVingtSix[loflVingtSix.index(item) + 1]
                    if prem[0] == VingtSix[0]:
                        if prem[1] not in VingtSix[1]:
                            prem[1] += ", "
                            prem[1] += VingtSix[1]
                            loflVingtSix[loflVingtSix.index(item)] = prem
                            del loflVingtSix[loflVingtSix.index(item) + 1]
                            
        # vingt-sept
        for i in range(3):
            for item in loflVingtSept:
                if loflVingtSept.index(item) != len(loflVingtSept) - 1:
                    prem = loflVingtSept[loflVingtSept.index(item)]
                    VingtSept = loflVingtSept[loflVingtSept.index(item) + 1]
                    if prem[0] == VingtSept[0]:
                        if prem[1] not in VingtSept[1]:
                            prem[1] += ", "
                            prem[1] += VingtSept[1]
                            loflVingtSept[loflVingtSept.index(item)] = prem
                            del loflVingtSept[loflVingtSept.index(item) + 1]
                            
        # vingt-huit
        for i in range(3):
            for item in loflVingtHuit:
                if loflVingtHuit.index(item) != len(loflVingtHuit) - 1:
                    prem = loflVingtHuit[loflVingtHuit.index(item)]
                    VingtHuit = loflVingtHuit[loflVingtHuit.index(item) + 1]
                    if prem[0] == VingtHuit[0]:
                        if prem[1] not in VingtHuit[1]:
                            prem[1] += ", "
                            prem[1] += VingtHuit[1]
                            loflVingtHuit[loflVingtHuit.index(item)] = prem
                            del loflVingtHuit[loflVingtHuit.index(item) + 1]
                            
        # vingt-neuf
        for i in range(3):
            for item in loflVingtNeuf:
                if loflVingtNeuf.index(item) != len(loflVingtNeuf) - 1:
                    prem = loflVingtNeuf[loflVingtNeuf.index(item)]
                    VingtNeuf = loflVingtNeuf[loflVingtNeuf.index(item) + 1]
                    if prem[0] == VingtNeuf[0]:
                        if prem[1] not in VingtNeuf[1]:
                            prem[1] += ", "
                            prem[1] += VingtNeuf[1]
                            loflVingtNeuf[loflVingtNeuf.index(item)] = prem
                            del loflVingtNeuf[loflVingtNeuf.index(item) + 1]
                            
        # trente
        for i in range(3):
            for item in loflTrente:
                if loflTrente.index(item) != len(loflTrente) - 1:
                    prem = loflTrente[loflTrente.index(item)]
                    Trente = loflTrente[loflTrente.index(item) + 1]
                    if prem[0] == Trente[0]:
                        if prem[1] not in Trente[1]:
                            prem[1] += ", "
                            prem[1] += Trente[1]
                            loflTrente[loflTrente.index(item)] = prem
                            del loflTrente[loflTrente.index(item) + 1]
                            
        # trente-et-un
        for i in range(3):
            for item in loflTrenteEtUn:
                if loflTrenteEtUn.index(item) != len(loflTrenteEtUn) - 1:
                    prem = loflTrenteEtUn[loflTrenteEtUn.index(item)]
                    TrenteEtUn = loflTrenteEtUn[loflTrenteEtUn.index(item) + 1]
                    if prem[0] == TrenteEtUn[0]:
                        if prem[1] not in TrenteEtUn[1]:
                            prem[1] += ", "
                            prem[1] += TrenteEtUn[1]
                            loflTrenteEtUn[loflTrenteEtUn.index(item)] = prem
                            del loflTrenteEtUn[loflTrenteEtUn.index(item) + 1]
                            
        # trente-deux
        for i in range(3):
            for item in loflTrenteDeux:
                if loflTrenteDeux.index(item) != len(loflTrenteDeux) - 1:
                    prem = loflTrenteDeux[loflTrenteDeux.index(item)]
                    TrenteDeux = loflTrenteDeux[loflTrenteDeux.index(item) + 1]
                    if prem[0] == TrenteDeux[0]:
                        if prem[1] not in TrenteDeux[1]:
                            prem[1] += ", "
                            prem[1] += TrenteDeux[1]
                            loflTrenteDeux[loflTrenteDeux.index(item)] = prem
                            del loflTrenteDeux[loflTrenteDeux.index(item) + 1]
                            
        # trente-trois
        for i in range(3):
            for item in loflTrenteTrois:
                if loflTrenteTrois.index(item) != len(loflTrenteTrois) - 1:
                    prem = loflTrenteTrois[loflTrenteTrois.index(item)]
                    TrenteTrois = loflTrenteTrois[loflTrenteTrois.index(item) + 1]
                    if prem[0] == TrenteTrois[0]:
                        if prem[1] not in TrenteTrois[1]:
                            prem[1] += ", "
                            prem[1] += TrenteTrois[1]
                            loflTrenteTrois[loflTrenteTrois.index(item)] = prem
                            del loflTrenteTrois[loflTrenteTrois.index(item) + 1]
                            
        # trente-quatre
        for i in range(3):
            for item in loflTrenteQuatre:
                if loflTrenteQuatre.index(item) != len(loflTrenteQuatre) - 1:
                    prem = loflTrenteQuatre[loflTrenteQuatre.index(item)]
                    TrenteQuatre = loflTrenteQuatre[loflTrenteQuatre.index(item) + 1]
                    if prem[0] == TrenteQuatre[0]:
                        if prem[1] not in TrenteQuatre[1]:
                            prem[1] += ", "
                            prem[1] += TrenteQuatre[1]
                            loflTrenteQuatre[loflTrenteQuatre.index(item)] = prem
                            del loflTrenteQuatre[loflTrenteQuatre.index(item) + 1]

        for part in range(total):
            del loflDeux[part][0]
            del loflTrois[part][0]
            del loflQuatre[part][0]
            del loflCinq[part][0]
            del loflSix[part][0]
            del loflSept[part][0]
            del loflHuit[part][0]
            del loflNeuf[part][0]
            del loflDix[part][0]
            del loflOnze[part][0]
            del loflDouze[part][0]
            del loflTreize[part][0]
            del loflQuatorze[part][0]
            del loflQuinze[part][0]
            del loflSeize[part][0]
            del loflDixSept[part][0]
            del loflDixHuit[part][0]
            del loflDixNeuf[part][0]
            del loflVingt[part][0]
            del loflVingtEtUn[part][0]
            del loflVingtDeux[part][0]
            del loflVingtTrois[part][0]
            del loflVingtQuatre[part][0]
            del loflVingtCinq[part][0]
            del loflVingtSix[part][0]
            del loflVingtSept[part][0]
            del loflVingtHuit[part][0]
            del loflVingtNeuf[part][0]
            del loflTrente[part][0]
            del loflTrenteEtUn[part][0]
            del loflTrenteDeux[part][0]
            del loflTrenteTrois[part][0]
            del loflTrenteQuatre[part][0]
            loflFin[part] = loflUn[part] + loflDeux[part] + loflTrois[part] + loflQuatre[part] + loflCinq[part] + loflSix[part] + loflSept[part] + loflHuit[part]\
                            + loflNeuf[part] + loflDix[part] + loflOnze[part] + loflDouze[part] + loflTreize[part] + loflQuatorze[part] + loflQuinze[part] + \
                            loflSeize[part] + loflDixSept[part] + loflDixHuit[part] + loflDixNeuf[part] + loflVingt[part] + loflVingtEtUn[part] + \
                            loflVingtDeux[part] + loflVingtTrois[part] + loflVingtQuatre[part] + loflVingtCinq[part] + loflVingtSix[part] + loflVingtSept[part] + \
                            loflVingtHuit[part] + loflVingtNeuf[part] + loflTrente[part] + loflTrenteEtUn[part] + loflTrenteDeux[part] + loflTrenteTrois[part] + \
                            loflTrenteQuatre[part]

        for row in loflFin:
            row_num += 1
            for col_num in range(len(row)):
                if isinstance(row[col_num], datetime.date):
                     style = date_style
                else:
                     style = font_style

                ws.write(row_num,col_num,row[col_num],style)

        wb.save(response)
        return response
