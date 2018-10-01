# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bdmultimedia.models import *
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import xlwt
from .filters import OutilFilter
from forms import Search
import datetime
import time


class DetailView(generic.DetailView):
    model = Outil
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['tout'] = Outil.objects.order_by('titre')
        context['liste'] = Outil.objects.all().values_list()
        return context


class AlaUneView(generic.ListView):
    #3 jours = 259200 secondes
    model = Outil
    template_name = 'aLaUne.html'
    context_object_name = 'outils'

    def get_queryset(self):
        request = self.request
        request.session['listeresultat'] = []
        # courrant = 18
        # liste = [79, 92, 93, 162, 125, 100, 45, 70, 102, 62, 98, 73, 19, 29, 67, 163, 17, 91, 142, 48, 149, 84, 40, 83, 90, 7, 127, 159, 122, 131, 138, 64, 31, 135, 75, 140, 25, 63, 14, 53, 126, 155, 28, 139, 115, 22, 37, 23, 44, 136, 10, 128, 117, 85, 76, 103, 151, 119, 107, 116, 4, 96, 130, 88, 1, 106, 66, 24, 143, 3, 153, 123, 134, 38, 13, 49, 146, 157, 27, 55, 20, 5, 56, 152, 54, 9, 112, 94, 113, 133, 121, 78, 43, 71, 51, 105, 36, 124, 87, 109, 21, 95, 58, 35, 158, 148, 26, 61, 8, 6, 89, 82, 32, 160, 50, 144, 65, 147, 52, 120, 97, 86, 141, 145, 137, 110, 99, 77, 16, 12, 47, 150, 72, 104, 81, 114, 132, 161, 111, 129, 42, 101, 34, 74]
        # for i in range(len(liste)):
        #     courrant = liste[i]
        #     time.sleep(30)


        return Outil.objects.order_by('titre')
        # return Outil.objects.get(pk=courrant)



class OutilDelete(generic.DeleteView):
    model = Outil
    success_url = reverse_lazy('home') # This is where this view will
                                            # redirect the user
    template_name = 'delete_outil.html'


class ListeView(generic.ListView):
    template_name = 'liste.html'
    context_object_name = 'all_outils'

    def get_queryset(self):
        return Outil.objects.order_by('titre')


class DeleteForm(generic.CreateView):
    model = Outil
    sucess_url = reverse_lazy('/')


class ListDetailView(generic.DetailView):
    model = Outil
    template_name = 'list_detail.html'

    def get_context_data(self, **kwargs):
        request = self.request
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['tout'] = request.session.get('listeresultat')
        context['toutrev'] = list(reversed(request.session.get('listeresultat')))
        return context


class OutilList(generic.View):
    def get(self, request):
        request = self.request

        data = OutilFilter(self.request.GET, queryset = Outil.objects.all().order_by('titre'))
        liste = []
        data_total = data.qs.count()
        all_main_registers = OutilFilter(self.request.GET, queryset=Outil.objects.all().order_by('titre'))
        for i in data.qs:
            liste.append(i.id)
        request.session['listeresultat'] = liste

        paginator = Paginator(data.qs, 40)
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


class SearchView(generic.ListView):
    template_name = 'recherche_motcle.html'
    paginate_by = 20
    def get_context_data(self, *args, **kwargs):
        context = super(SearchView,self).get_context_data(*args, **kwargs)
        if self.request.GET.get('q') is not None:
            context['count'] = self.count
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        remplacements = [
                             ("contemporaine","contemporain"),
                             ("lyrique","opéra"),
                             ("post-romantisme", "postromantique"),
                             ("romantisme","romantique"),
                             ("post-romantique","postromantique"),
                             ("néo-classicisme","néoclassique"),
                             ("classicisme","classique"),
                             ("néo-classique","néoclassique"),
                             ("minimaliste","minimalisme"),
                             ("postmodernisme", "post-moderne"),
                             ("modernisme","moderne"),
                             ("postmoderne","post-moderne"),
                             ("orientalisme", "orientaliste"),
                             ("orientale", "orientaliste"),
                             ("veriste","verisme"),
                             ("ieme siecle","è"),("ieme siècle", "è"),("ième siecle", "è"),("ième siècle", "è"),
                             ("e siecle","è"),("e siècle","è"),("è siècle",""),("è",""),
                             ("d'",""),("c'",""),("j'",""),("l'",""),("m'",""),("jusqu'",""),("n'",""),("puisqu'",""),
                             ("quelqu'", ""),("qu'", ""),("s'",""),("t'",""),
                        ]
        mots_vides =[
                         "musique","elle","il","10ème","1er","1ère","2ème","3ème","4ème","5ème","6ème",
                         "7ème","8ème","9ème"," a","afin","ai","ainsi","ais","ait","alors","apres","as",
                         "assez","au","aucun","aucune","aupres","auquel","auquelles","auquels","auraient","aurais",
                         "aurait","aurez","auriez","aurions","aurons","auront","aussi","aussitot","autre","autres","aux",
                         "avaient","avais","avait","avant","avec","avez","aviez","avoir","avons","ayant","beaucoup",
                         "car","ce","ceci","cela","celle","celles","celui","cependant","certes","ces","cet","cette",
                         "ceux","chacun","chacune","chaque","chez","cinq","comme","d'abord","dans","de","dehors",
                         "dela","depuis","des","dessous","dessus","deux","deca","dix","doit","donc","dont","du","durant",
                         "des","deja","elle","elles","en","encore","enfin","entre","er","est","est-ce","et","etc",
                         "eu","eurent","eut","faut","fur","hormis","hors","huit","il","ils","je",
                         "la","laquelle","le","lequel","les","lesquels","leur","leurs","lors","lorsque","lui","la",
                         "mais","malgre","me","melle","mes","mm","mme","moi","moins","mon","mr","meme","memes"
                         "neuf","ni","non-","nos","notamment","notre","nous","neanmoins","notres","on","ont","ou","ou",
                         "par","parce","parfois","parmi","partout","pas","pendant","peu","peut","peut-etre","plus","plutot",
                         "pour","pourquoi","pres","puisque","quand","quant","quatre","quel","quelle",
                         "quelles","quelque","quelquefois","quelques","quels","qui","quoi","quot","sa","sans",
                         "se","sept","sera","serai","seraient","serais","serait","seras","serez","seriez","serions","serons",
                         "seront","ses","si","sien","siennes","siens","sitot","six","soi","sommes","son","sont","sous",
                         "souvent","suis","sur","toi","ton","toujours","tous","tout","toutefois","toutes","trois",
                         "tu","un","une","unes","uns","voici","voila","vos","votre","vous","votres","y",
                         "eme","etaient","etais","etait","etant","etiez","etions","etes","etre","afin","ainsi","alors",
                         "apres","aucun","aucune","aupres","auquel","aussi","autant","aux","avec","car","ceci","cela",
                         "celle","celles","celui","cependant","ces","cet","cette","ceux","chacun","chacune","chaque",
                         "chez","comme","comment","dans","des","donc","donne","dont","duquel","des","déjà","elle",
                         "elles","encore","entre","etant","etc","eux","furent","grace","hors","ici","ils",
                         "jusqu","les","leur","leurs","lors","lui","mais","malgre","mes","mien","mienne","miennes",
                         "miens","moins","moment"," mon"," meme","memes"," non","nos","notre","notres","nous","notre",
                         "oui","par","parce","parmi","plus","pour","pres","puis","puisque","quand","quant","quel",
                         "quelle","quelque","quelquun","quelques","quels","qui","quoi","sans","sauf","selon","ses",
                         "sien","sienne","siennes","siens","soi","soit","sont","sous","suis","sur","tandis","tant","tes",
                         "tienne","tiennes","tiens","toi","ton","tous","tout","toute","toutes","trop","très","une",
                         "vos","votre","vous","étaient","était","étant","être",
                    ]

        if query is not None:
            query = query.lower()
            for i in remplacements:
                if i[0] in query:
                    query = query.replace(i[0], i[1])

            mots = dum = query.split(" ")
            for i in dum:
                if i in mots_vides:
                    mots.remove(i)

            if len(mots) >= 1 and query != "":
                results = Outil.objects.search(query=mots[0]).order_by('titre')
                tempo = []
                for i in mots:
                    if i != mots[0]:
                        for j in Outil.objects.search(query=i).order_by('titre'):
                            if j in results:
                                tempo.append(j)
                        results = tempo
                        tempo = []

            else:
                results = Outil.objects.order_by('titre')

            qs = list(results)
            liste = []
            for i in results:
                liste.append(i.id)
            self.count = len(qs)
            # pour pouvoir naviguer entre les fiches (précédent + suivant)
            request.session['listeresultat'] = liste
            return results
        return Outil.objects.none()


class GererView(generic.ListView):
    template_name = 'gerer.html'

    def get_queryset(self):
        return Outil.objects.all()


class GererProdType(generic.ListView):
    model = ProdType
    template_name = 'gerer_prodType.html'
    context_object_name = 'all_prodType'
    liste = ProdType.objects.order_by('nom')

    def get_queryset(self):
        return GererProdType.liste


class GererProducteurNom(generic.ListView):
    model = ProducteurNom
    template_name = 'gerer_producteurNom.html'
    context_object_name = 'all_producteurNom'
    liste = ProducteurNom.objects.order_by('nom')

    def get_queryset(self):
        return GererProducteurNom.liste


class GererSupportDiffusion(generic.ListView):
    model = SupportDiffusion
    template_name = 'gerer_supportDiffusion.html'
    context_object_name = 'all_supportDiffusion'
    liste = SupportDiffusion.objects.order_by('nom')

    def get_queryset(self):
        return GererSupportDiffusion.liste


class GererFormatOutil(generic.ListView):
    model = FormatOutil
    template_name = 'gerer_formatOutil.html'
    context_object_name = 'all_formatOutil'
    liste = FormatOutil.objects.order_by('nom')

    def get_quertset(self):
        return GererFormatOutil.liste


class GererFormeNarrative(generic.ListView):
    model = FormeNarrative
    template_name = 'gerer_formeNarrative.html'
    context_object_name = 'all_formeNarrative'
    liste = FormeNarrative.objects.order_by('nom')

    def get_queryset(self):
        return GererFormeNarrative.liste


class GererModeHebergement(generic.ListView):
    model = ModeHebergement
    template_name = 'gerer_modeHebergement.html'
    context_object_name = 'all_modeHebergement'
    liste = ModeHebergement.objects.order_by('nom')

    def get_queryset(self):
        return GererModeHebergement.liste


class GererModeConsultation(generic.ListView):
    model = ModeConsultation
    template_name = 'gerer_modeConsultation.html'
    context_object_name = 'all_modeConsultation'
    liste = ModeConsultation.objects.order_by('nom')

    def get_queryset(self):
        return GererModeConsultation.liste


class GererLangueNarration(generic.ListView):
    model = LangueNarration
    template_name = 'gerer_langueNarration.html'
    context_object_name = 'all_langueNarration'
    liste = LangueNarration.objects.order_by('nom')

    def get_queryset(self):
        return GererLangueNarration.liste


class GererSousTitre(generic.ListView):
    model = SousTitre
    template_name = 'gerer_sousTitre.html'
    context_object_name = 'all_sousTitre'
    liste = SousTitre.objects.order_by('nom')

    def get_queryset(self):
        return GererSousTitre.liste


class GererOrchestration(generic.ListView):
    model = Orchestration
    template_name = 'gerer_orchestration.html'
    context_object_name = 'all_orchestration'
    liste = Orchestration.objects.order_by('nom')

    def get_queryset(self):
        return GererOrchestration.liste


class GererStructure(generic.ListView):
    model = Structure
    template_name = 'gerer_structure.html'
    context_object_name = 'all_structure'
    liste = Structure.objects.order_by('nom')

    def get_queryset(self):
        return GererStructure.liste


class GererLanguageMusical(generic.ListView):
    model = LanguageMusical
    template_name = 'gerer_languageMusical.html'
    context_object_name = 'all_languageMusical'
    liste = LanguageMusical.objects.order_by('nom')

    def get_queryset(self):
        return GererLanguageMusical.liste


class GererGenreMusical(generic.ListView):
    model = GenreMusical
    template_name = 'gerer_genreMusical.html'
    context_object_name = 'all_genreMusical'
    liste = GenreMusical.objects.order_by('nom')

    def get_queryset(self):
        return GererGenreMusical.liste


class GererStyleMusical(generic.ListView):
    model = StyleMusical
    template_name = 'gerer_styleMusical.html'
    context_object_name = 'all_styleMusical'
    liste = StyleMusical.objects.order_by('nom')

    def get_queryset(self):
        return GererStyleMusical.liste


class GererExperienceMusicale(generic.ListView):
    model = ExperienceMusicale
    template_name = 'gerer_experienceMusicale.html'
    context_object_name = 'all_experienceMusicale'
    liste = ExperienceMusicale.objects.order_by('nom')

    def get_queryset(self):
        return GererExperienceMusicale.liste


class GererContexte(generic.ListView):
    model = Contexte
    template_name = "gerer_contexte.html"
    context_object_name = 'all_contexte'
    liste = Contexte.objects.order_by('nom')

    def get_queryset(self):
        return GererContexte.liste


class GererRoleEvolution(generic.ListView):
    model = RoleEvolution
    template_name = 'gerer_roleEvolution.html'
    context_object_name = 'all_roleEvolution'
    liste = RoleEvolution.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleEvolution.liste


class GererOrganologie(generic.ListView):
    model = Organologie
    template_name = 'gerer_organologie.html'
    context_object_name = 'all_organologie'
    liste = Organologie.objects.order_by('nom')

    def get_queryset(self):
        return GererOrganologie.liste


class GererSollicitationMusicale(generic.ListView):
    model = SollicitationMusicale
    template_name = 'gerer_sollicitationMusicale.html'
    context_object_name = 'all_sollicitationMusicale'
    liste = SollicitationMusicale.objects.order_by('nom')

    def get_queryset(self):
        return GererSollicitationMusicale.liste


class GererSollicitationGenerale(generic.ListView):
    model = SollicitationGenerale
    template_name = 'gerer_sollicitationGenerale.html'
    context_object_name = 'all_sollicitationGenerale'
    liste = SollicitationGenerale.objects.order_by('nom')

    def get_queryset(self):
        return GererSollicitationGenerale.liste


class GererEvocationGraphique(generic.ListView):
    model = EvocationGraphique
    template_name = 'gerer_evocationGraphique.html'
    context_object_name = 'all_evocationGraphique'
    liste = EvocationGraphique.objects.order_by('nom')

    def get_queryset(self):
        return GererEvocationGraphique.liste


class GererEvocationPlastique(generic.ListView):
    model = EvocationPlastique
    template_name = 'gerer_evocationPlastique.html'
    context_object_name = 'all_evocationPlastique'
    liste = EvocationPlastique.objects.order_by('nom')

    def get_queryset(self):
        return GererEvocationPlastique.liste
    

class GererEvocationAutre(generic.ListView):
    model = EvocationAutre
    template_name = 'gerer_evocationAutre.html'
    context_object_name = 'all_evocationAutre'
    liste = EvocationAutre.objects.order_by('nom')

    def get_queryset(self):
        return GererEvocationAutre.liste


class GererNotionsInter(generic.ListView):
    model = NotionsInter
    template_name = 'gerer_notionsInter.html'
    context_object_name = 'all_notionsInter'
    liste = NotionsInter.objects.order_by('nom')

    def get_queryset(self):
        return GererNotionsInter.liste


class GererRoleFemmes(generic.ListView):
    model = RoleFemmes
    template_name = 'gerer_roleFemmes.html'
    context_object_name = 'all_roleFemmes'
    liste = RoleFemmes.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleFemmes.liste


class GererRoleHommes(generic.ListView):
    model = RoleHomme
    template_name = 'gerer_roleHommes.html'
    context_object_name = 'all_roleHommes'
    liste = RoleHomme.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleHommes.liste


class GererRoleHumainNeutre(generic.ListView):
    model = RoleHumainNeutre
    template_name = 'gerer_roleHumainNeutre.html'
    context_object_name = 'all_roleHumainNeutre'
    liste = RoleHumainNeutre.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleHumainNeutre.liste


class GererRolePersAnimFemmes(generic.ListView):
    model = RolePersAnimFemmes
    template_name = 'gerer_rolePersAnimFemmes.html'
    context_object_name = 'all_rolePersAnimFemmes'
    liste = RolePersAnimFemmes.objects.order_by('nom')
    
    def get_queryset(self):
        return GererRolePersAnimFemmes.liste
    
    
class GererRolePersAnimHommes(generic.ListView):
    model = RolePersAnimHomme
    template_name = 'gerer_rolePersAnimHommes.html'
    context_object_name = 'all_rolePersAnimHommes'
    liste = RolePersAnimHomme.objects.order_by('nom')
    
    def get_queryset(self):
        return GererRolePersAnimHommes.liste


class GererRolePersAnimNeutre(generic.ListView):
    model = RolePersAnimNeutre
    template_name = 'gerer_rolePersAnimNeutre.html'
    context_object_name = 'all_rolePersAnimNeutre'
    liste = RolePersAnimNeutre.objects.order_by('nom')

    def get_queryset(self):
        return GererRolePersAnimNeutre.liste


class GererRoleAnimauxFemmes(generic.ListView):
    model = RoleAnimauxFemmes
    template_name = 'gerer_roleAnimauxFemmes.html'
    context_object_name = 'all_roleAnimauxFemmes'
    liste = RoleAnimauxFemmes.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleAnimauxFemmes.liste


class GererRoleAnimauxHommes(generic.ListView):
    model = RoleAnimauxHomme
    template_name = 'gerer_roleAnimauxHommes.html'
    context_object_name = 'all_roleAnimauxHommes'
    liste = RoleAnimauxHomme.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleAnimauxHommes.liste


class GererRoleAnimauxNeutre(generic.ListView):
    model = RoleAnimauxNeutre
    template_name = 'gerer_roleAnimauxNeutre.html'
    context_object_name = 'all_roleAnimauxNeutre'
    liste = RoleAnimauxNeutre.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleAnimauxNeutre.liste


class GererRoleInstrFemmes(generic.ListView):
    model = RoleInstrFemmes
    template_name = 'gerer_roleInstrFemmes.html'
    context_object_name = 'all_roleInstrFemmes'
    liste = RoleInstrFemmes.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleInstrFemmes.liste


class GererRoleInstrHommes(generic.ListView):
    model = RoleInstrHomme
    template_name = 'gerer_roleInstrHommes.html'
    context_object_name = 'all_roleInstrHommes'
    liste = RoleInstrHomme.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleInstrHommes.liste


class GererRoleInstrNeutre(generic.ListView):
    model = RoleInstrNeutre
    template_name = 'gerer_roleInstrNeutre.html'
    context_object_name = 'all_roleInstrNeutre'
    liste = RoleInstrNeutre.objects.order_by('nom')

    def get_queryset(self):
        return GererRoleInstrNeutre.liste


def export_xls(request):
    if request.user.is_authenticated():
        response = HttpResponse(content_type='application/ms-excel')
        aujourdui = datetime.datetime.now().strftime('%d/%m/%Y')
        nom = "[" + aujourdui + "]_Catalogue_raisonné_de_dispositifs_numérique.xls"
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
                   "R.11 Date de mise en ligne", "R.12 Date du dépouillement", "R.13 Interactivite", "R.13.1 Doccuments à imprimer",
                   "R.14 Personnification du service","R.15 Possibilité de laisser des commentaires", "R.16 Nombre de commentaires",
                   "S.17 Premier Onglet","S.17.1 Autre - Premier Onglet","S.18 Deuxième Onglet","S.18.1 Autre - Deuxième Onglet",
                   "S.19 Troisième Onglet","S19.1 Autre Troisième Onglet","S.19. 1 PLUS DE TROIS ONGLETS à ouvrir pour trouver ce dispositif ?","S.20 Mode d'hébergement","S.21 Mode de consultation",
                   "S.22 langue de la narration","S.23 Sous-titrages", "S.24.1 Accessible aux malentendants","S.24.2 Accessible aux malvoyants",
                   "M.25 Matériau musical (parle-t-on)","M.25.1 Orchestration (parle-t-on)",
                   "M.25.2 Structure (parle-t-on)", "M.25.3 language musical (parle-t-on)","M.25.4 Genre musical (parle-t-on)l", "M.25.5 Style musical (parle-t-on)",
                   "M.26 Expérience musicale (parle-t-on)", "M.27 Éléments sociocultutrels et historique (parle-t-on)", "M.27.1 Époque",
                   "M.27.2 Contexte de composition, création, interprétation", "U.27.3 Rôle de l'évolution", "M.27.4 Organologie (parle-t-on)",
                   "U.28 Sollicitation musicale", "U.29 Sollicifation générale", "PM.30 Temps de musique", "PM.31 Temps de parole", "PM.32 Temps musique et parole",
                   "PM.33 Mise en valeur du sonore", "EM.34 Évocation graphique", "EM.35 Évocation plastique", "EM.36 Évocation litteraire",
                   "EM.37 Autre discipline évoquée", "I.38 Notions communes", "I.38 Expérience", "I.38 Pratique",
                   "I.39 Exemples de notions évoquées de façon interdisciplinaires", "STÉ.39.1 Nombre total d'humains", "STÉ.39.1 Nombre d'hommes",
                   "STÉ.39.1 Nombre de femmes","STÉ.39.1 Nombre d'humains au genre indéterminé", "Sté.39.2 Rôle des femmes", "Sté.39.3 Rôle des hommes",
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

        loftUn = list(Outil.objects.order_by('titre').values_list('titre','url','site','ensemble_thematique','ensemble_thematique_nom', 'producteur_type__nom'))
        loflUn = [list(elem) for elem in loftUn]
        loftUnUn = list(Outil.objects.order_by('titre').values_list('titre','producteur_nom__nom'))
        loflUnUn = [list(elem) for elem in loftUnUn]
        loftDeux = list(Outil.objects.order_by('titre').values_list('titre','support_diffusion__nom'))
        loflDeux = [list(elem) for elem in loftDeux]
        loftTrois = list(Outil.objects.order_by('titre').values_list('titre','format__nom'))
        loflTrois = [list(elem) for elem in loftTrois]
        loftQuatre = list(Outil.objects.order_by('titre').values_list('titre','forme_narrative__nom','duree','nb_pages','mise_en_ligne_date','depouillement_date','interactivite','materiel_imprimer',
                                                          'personnification_service','commentaire_possible','commentaire_nombre','premier_onglet', 'prem_onglet_autre',
                                                          'deuxieme_onglet', 'deux_onglet_autre', 'troisieme_onglet', 'trois_onglet_autre','plus_de_tois_onglet'))
        loflQuatre = [list(elem) for elem in loftQuatre]
        loftCinq = list(Outil.objects.order_by('titre').values_list('titre','mode_hebergement__nom'))
        loflCinq = [list(elem) for elem in loftCinq]
        loftSix = list(Outil.objects.order_by('titre').values_list('titre','mode_consultation__nom'))
        loflSix = [list(elem) for elem in loftSix]
        loftSept = list(Outil.objects.order_by('titre').values_list('titre','narration_langue__nom'))
        loflSept = [list(elem) for elem in loftSept]
        loftHuit = list(Outil.objects.order_by('titre').values_list('titre','sous_titre__nom', 'malentendants', 'malvoyants', 'materiau_musical'))
        loflHuit = [list(elem) for elem in loftHuit]
        loftNeuf = list(Outil.objects.order_by('titre').values_list('titre','orchestration__nom'))
        loflNeuf = [list(elem) for elem in loftNeuf]
        loftDix = list(Outil.objects.order_by('titre').values_list('titre','structure__nom'))
        loflDix = [list(elem) for elem in loftDix]
        loftOnze = list(Outil.objects.order_by('titre').values_list('titre','language_musical__nom'))
        loflOnze = [list(elem) for elem in loftOnze]
        loftDouze = list(Outil.objects.order_by('titre').values_list('titre','genre_musical__nom'))
        loflDouze = [list(elem) for elem in loftDouze]
        loftTreize = list(Outil.objects.order_by('titre').values_list('titre','style_musical__nom'))
        loflTreize = [list(elem) for elem in loftTreize]
        loftQuatorze = list(Outil.objects.order_by('titre').values_list('titre','experience_musicale__nom', 'elements_socioculturels', 'epoque'))
        loflQuatorze = [list(elem) for elem in loftQuatorze]

        #loftepoque = list(Outil.objects.order_by('titre').values_list('epoque'))
        #loflepoque = [list(elem) for elem in loftepoque]

        loftQuinze = list(Outil.objects.order_by('titre').values_list('titre','contexte__nom'))
        loflQuinze = [list(elem) for elem in loftQuinze]
        loftSeize = list(Outil.objects.order_by('titre').values_list('titre','role_evolution__nom'))
        loflSeize = [list(elem) for elem in loftSeize]
        loftSeizeDeux = list(Outil.objects.order_by('titre').values_list('titre','organologie__nom')) #organologie
        loflSeizeDeux = [list(elem) for elem in loftSeizeDeux]
        loftDixSept = list(Outil.objects.order_by('titre').values_list('titre','sollicitation_musicale__nom'))
        loflDixSept = [list(elem) for elem in loftDixSept]
        loftDixHuit = list(Outil.objects.order_by('titre').values_list('titre','sollicitation_generale__nom', 'temps_mus', 'temps_par', 'temps_mus_par', 'sonore_valeur'))
        loflDixHuit = [list(elem) for elem in loftDixHuit]
        loftDixNeuf = list(Outil.objects.order_by('titre').values_list('titre', 'evocation_graphique__nom'))
        loflDixNeuf = [list(elem) for elem in loftDixNeuf]
        loftVingt = list(Outil.objects.order_by('titre').values_list('titre', 'evocation_plastique__nom', 'evocation_litteraire'))
        loflVingt = [list(elem) for elem in loftVingt]
        loftVingtEtUn = list(Outil.objects.order_by('titre').values_list('titre', 'evocation_autre__nom', 'notion_concepts', 'notion_experiences', 'notion_pratiques'))
        loflVingtEtUn = [list(elem) for elem in loftVingtEtUn]
        loftVingtDeux = list(Outil.objects.order_by('titre').values_list('titre', 'exemples_notions_interdisciplinaires__nom', 'nb_humains_total', 'nb_hommes', 'nb_femmes',
                                                             'nb_humains_indetermines'))
        loflVingtDeux = [list(elem) for elem in loftVingtDeux]
        loftVingtTrois = list(Outil.objects.order_by('titre').values_list('titre', 'role_humain_femme__nom'))
        loflVingtTrois = [list(elem) for elem in loftVingtTrois]
        loftVingtQuatre = list(Outil.objects.order_by('titre').values_list('titre', 'role_humain_homme__nom'))
        loflVingtQuatre = [list(elem) for elem in loftVingtQuatre]
        loftVingtCinq = list(Outil.objects.order_by('titre').values_list('titre', 'role_humain_neutre__nom', 'nb_pers_anime_total', 'nb_pers_anime_hommes',
                                                             'nb_pers_anime_femmes', 'nb_pers_anime_indetermines'))
        loflVingtCinq = [list(elem) for elem in loftVingtCinq]
        loftVingtSix = list(Outil.objects.order_by('titre').values_list('titre', 'role_pers_anime_femme__nom'))
        loflVingtSix = [list(elem) for elem in loftVingtSix]
        loftVingtSept = list(Outil.objects.order_by('titre').values_list('titre', 'role_pers_anime_homme__nom'))
        loflVingtSept = [list(elem) for elem in loftVingtSept]
        loftVingtHuit = list(Outil.objects.order_by('titre').values_list('titre', 'role_pers_anime_neutre__nom', 'nb_animaux_total', 'nb_males', 'nb_femelles',
                                                             'nb_animaux_indetermines'))
        loflVingtHuit = [list(elem) for elem in loftVingtHuit]
        loftVingtNeuf = list(Outil.objects.order_by('titre').values_list('titre', 'role_animaux_femme__nom'))
        loflVingtNeuf = [list(elem) for elem in loftVingtNeuf]
        loftTrente = list(Outil.objects.order_by('titre').values_list('titre', 'role_animaux_homme__nom'))
        loflTrente = [list(elem) for elem in loftTrente]
        loftTrenteEtUn = list(Outil.objects.order_by('titre').values_list('titre','role_animaux_neutre__nom', 'nb_instr_anime_total', 'nb_instr_anime_hommes',
                                                              'nb_instr_anime_femmes', 'nb_instr_anime_indetermines'))
        loflTrenteEtUn = [list(elem) for elem in loftTrenteEtUn]
        loftTrenteDeux = list(Outil.objects.order_by('titre').values_list('titre', 'role_instr_anime_femme__nom'))
        loflTrenteDeux = [list(elem) for elem in loftTrenteDeux]
        loftTrenteTrois = list(Outil.objects.order_by('titre').values_list('titre', 'role_instr_anime_homme__nom'))
        loflTrenteTrois = [list(elem) for elem in loftTrenteTrois]
        loftTrenteQuatre = list(Outil.objects.order_by('titre').values_list('titre', 'role_instr_anime_neutre__nom'))
        loflTrenteQuatre = [list(elem) for elem in loftTrenteQuatre]
        
        total = Outil.objects.all().count()

        loflFin = [None] * total


        # BOUCLES POUR JOINDRE LES "MANYTOMANYFILEDS" DANS UN STRING
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

        # UnUn
        for i in range(4):
            for item in loflUnUn:
                if loflUnUn.index(item) != len(loflUnUn) - 1:
                    prem = loflUnUn[loflUnUn.index(item)]
                    deux = loflUnUn[loflUnUn.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[1] not in deux[1]:
                            prem[1] += ", "
                            prem[1] += deux[1]
                            loflUnUn[loflUnUn.index(item)] = prem
                            del loflUnUn[loflUnUn.index(item) + 1]

        # deux
        for i in range(4):
            for item in loflDeux:
                if loflDeux.index(item) != len(loflDeux) - 1:
                    prem = loflDeux[loflDeux.index(item)]
                    deux = loflDeux[loflDeux.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[1] not in deux[1]:
                            prem[1] += ", "
                            prem[1] += deux[1]
                            loflDeux[loflDeux.index(item)] = prem
                            del loflDeux[loflDeux.index(item) + 1]

        # trois
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        
        # seize-deux
        for i in range(4):
            for item in loflSeizeDeux:
                if loflSeizeDeux.index(item) != len(loflSeizeDeux) - 1:
                    prem = loflSeizeDeux[loflSeizeDeux.index(item)]
                    SeizeDeux = loflSeizeDeux[loflSeizeDeux.index(item) + 1]
                    if prem[0] == SeizeDeux[0]:
                        if prem[1] not in SeizeDeux[1]:
                            prem[1] += ", "
                            prem[1] += SeizeDeux[1]
                            loflSeizeDeux[loflSeizeDeux.index(item)] = prem
                            del loflSeizeDeux[loflSeizeDeux.index(item) + 1]
        
        # dix-sept
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
        for i in range(4):
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
            del loflUnUn[part][0]
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
            del loflSeizeDeux[part][0]
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
            loflFin[part] = loflUn[part] + loflUnUn[part] + loflDeux[part] + loflTrois[part] + loflQuatre[part] + loflCinq[part] + loflSix[part] + loflSept[part] + loflHuit[part]\
                            + loflNeuf[part] + loflDix[part] + loflOnze[part] + loflDouze[part] + loflTreize[part] + loflQuatorze[part] + loflQuinze[part] + \
                            loflSeize[part] + loflSeizeDeux[part] + loflDixSept[part] + loflDixHuit[part] + loflDixNeuf[part] + loflVingt[part] + loflVingtEtUn[part] + \
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
