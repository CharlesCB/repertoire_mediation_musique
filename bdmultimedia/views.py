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
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class DetailView(generic.DetailView):
    model = Outil
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['tout'] = Outil.objects.order_by('titre')
        context['liste'] = Outil.objects.all().values_list()
        return context


class AlaUneView(generic.ListView):
    # 3 jours = 259200 secondes
    model = Outil
    template_name = 'aLaUne.html'
    context_object_name = 'outils'

    def get_queryset(self):
        request = self.request
        request.session['listeresultat'] = []

        return Outil.objects.order_by('titre')


def sinscrire(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, groups=2)
            login(request, user)
            return redirect('aLaUne')
    else:
        form = UserCreationForm()
    return render(request, 'sinscrire.html', {'form': form})


class ListeView(generic.ListView):
    template_name = 'liste.html'
    context_object_name = 'all_outils'

    def get_queryset(self):
        lettre = self.request.GET.get('q')
        if lettre == "digit":
            return Outil.objects.filter((Q(titre__istartswith='0') |
                                         Q(titre__istartswith='1') |
                                         Q(titre__istartswith='2') |
                                         Q(titre__istartswith='3') |
                                         Q(titre__istartswith='4') |
                                         Q(titre__istartswith='5') |
                                         Q(titre__istartswith='6') |
                                         Q(titre__istartswith='7') |
                                         Q(titre__istartswith='8') |
                                         Q(titre__istartswith='9'))).distinct().order_by('titre')
        else:
            return Outil.objects.filter(titre__istartswith=lettre).order_by('titre')


def outil_delete(request, pk):
    outil = get_object_or_404(Outil, pk=pk)  # Get your current object

    if request.method == 'POST':         # If method is POST,
        outil.delete()                     # delete the cat.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'detail.html', {'outil': outil})


class ListDetailView(generic.DetailView):
    model = Outil
    template_name = 'list_detail.html'

    def get_context_data(self, **kwargs):
        request = self.request
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['tout'] = request.session.get('listeresultat')
        context['toutrev'] = reversed(request.session.get('listeresultat'))
        return context


class OutilList(generic.View):
    def get(self, request):
        request = self.request
        sort = request.GET.get('sort', 'titre')
        orders = [sort,'depouillement_date']

        data = OutilFilter(self.request.GET, queryset = Outil.objects.all().order_by(*orders))
        liste = []
        data_total = data.qs.count()
        all_main_registers = OutilFilter(self.request.GET, queryset=Outil.objects.all().order_by('titre'))
        for i in data.qs:
            liste.append(i.pk)
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
        context['temps'] = self.request.session.get('tempsRequete')
        return context

    def get_queryset(self):
        request = self.request
        temps_initial = time.time()
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
                             ("jeux","jouer"),
                             ("unisson","homophonie"),
                             ("motivique","motif"),
                             #("sérialisme","dodécaphonisme"),
                             #("sérielle", "dodécaphonisme"),
                             ("participatif","participation"),
                             ("religion","religieu"),
                             ("histoire","histo"),
                             ("historique","histo"),
                             ("bricolage","bricoler"),
                             ("conférence","conférenc"),
                             ("conférencier","conférenc"),
                             ("conférencière","conférenc"),
                             ("ieme siecle","è"),("ieme siècle", "è"),("ième siecle", "è"),("ième siècle", "è"),
                             ("e siecle","è"),("e siècle","è"),("è siècle",""),
                             ("d'",""),("c'",""),("j'",""),("l'",""),("m'",""),("jusqu'",""),("n'",""),("puisqu'",""),
                             ("quelqu'", ""),("qu'", ""),("s'",""),("t'",""),
                        ]
        mots_vides =[
                         "musique","elle","il","10ème","1er","1ère","2ème","3ème","4ème","5ème","6ème",
                         "7ème","8ème","9ème"," a","afin","ai","ainsi","ais","ait","alors","apres","as",
                         "assez","au","aucun","aucune","aupres","auquel","auquelles","auquels","auraient","aurais",
                         "aurait","aurez","auriez","aurions","aurons","auront","aussi","aussitot","autre","autres","aux",
                         "avaient","avais","avait","avec","avez","aviez","avoir","avons","ayant","beaucoup",
                         "car","ce","ceci","cela","celle","celles","celui","cependant","certes","ces","cet","cette",
                         "ceux","chacun","chacune","chaque","chez","cinq","comme","d'abord","dans","de","dehors",
                         "dela","depuis","des","dessous","dessus","deux","deca","dix","doit","donc","dont","du","durant",
                         "des","deja","elle","elles","en","encore","enfin","entre","er","est","est-ce","et","etc",
                         "eu","eurent","eut","faut","fur","hormis","hors","huit","il","ils","je",
                         "la","laquelle","le","lequel","les","lesquels","leur","leurs","lors","lorsque","lui",
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
                         "vos","votre","vous","étaient","était","étant","être"
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
                results = Outil.objects.search(query=mots[0])
                tempo = []
                for i in mots:
                    if i != mots[0]:
                        for j in Outil.objects.search(query=i):
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

            temps = time.time() - temps_initial
            request.session['tempsRequete'] = temps
            return results
        return list(Outil.objects.none().order_by('titre'))


class GererProdType(generic.ListView):
    model = ProdType
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererProdType, self).get_context_data(**kwargs)
        context['liste'] = ProdType.objects.order_by('nom')
        context['nom'] = 'prodtype'
        context['verbose'] = 'types de producteurs'
        return context


class GererProducteurNom(generic.ListView):
    model = ProducteurNom
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererProducteurNom, self).get_context_data(**kwargs)
        context['liste'] = ProducteurNom.objects.order_by('nom')
        context['nom'] = 'producteurnom'
        context['verbose'] = 'noms de producteurs'
        return context


class GererSupportDiffusion(generic.ListView):
    model = SupportDiffusion
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererSupportDiffusion, self).get_context_data(**kwargs)
        context['liste'] = SupportDiffusion.objects.order_by('nom')
        context['nom'] = 'supportdiffusion'
        context['verbose'] = 'supports de diffusion'
        return context


class GererFormatOutil(generic.ListView):
    model = FormatOutil
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererFormatOutil, self).get_context_data(**kwargs)
        context['liste'] = FormatOutil.objects.order_by('nom')
        context['nom'] = 'formatoutil'
        context['verbose'] = 'formats de dispositif'
        return context


class GererFormeNarrative(generic.ListView):
    model = FormeNarrative
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererFormeNarrative, self).get_context_data(**kwargs)
        context['liste'] = FormeNarrative.objects.order_by('nom')
        context['nom'] = 'formenarrative'
        context['verbose'] = 'formes narratives'
        return context


class GererModeHebergement(generic.ListView):
    model = ModeHebergement
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererModeHebergement, self).get_context_data(**kwargs)
        context['liste'] = ModeHebergement.objects.order_by('nom')
        context['nom'] = 'modehebergement'
        context['verbose'] = "modes d'hébergement"
        return context


class GererModeConsultation(generic.ListView):
    model = ModeConsultation
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererModeConsultation, self).get_context_data(**kwargs)
        context['liste'] = ModeConsultation.objects.order_by('nom')

        context['nom'] = 'modeconsultation'
        context['verbose'] = 'modes de consultation'
        return context


class GererLangueNarration(generic.ListView):
    model = LangueNarration
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererLangueNarration, self).get_context_data(**kwargs)
        context['liste'] = LangueNarration.objects.order_by('nom')
        context['nom'] = 'languenarration'
        context['verbose'] = 'langues de dispositif'
        return context


class GererSousTitre(generic.ListView):
    model = SousTitre
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererSousTitre, self).get_context_data(**kwargs)
        context['liste'] = SousTitre.objects.order_by('nom')
        context['nom'] = 'soustitre'
        context['verbose'] = 'sous-titres'
        return context


class GererOrchestration(generic.ListView):
    model = Orchestration
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererOrchestration, self).get_context_data(**kwargs)
        context['liste'] = Orchestration.objects.order_by('nom')
        context['nom'] = 'orchestration'
        context['verbose'] = "notions d'orchestration"
        return context


class GererStructure(generic.ListView):
    model = Structure
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererStructure, self).get_context_data(**kwargs)
        context['liste'] = Structure.objects.order_by('nom')
        context['nom'] = 'structure'
        context['verbose'] = "structures"
        return context


class GererLanguageMusical(generic.ListView):
    model = LanguageMusical
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererLanguageMusical, self).get_context_data(**kwargs)
        context['liste'] = LanguageMusical.objects.order_by('nom')
        context['nom'] = 'languagemusical'
        context['verbose'] = "notions de language musical"
        return context


class GererGenreMusical(generic.ListView):
    model = GenreMusical
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererGenreMusical, self).get_context_data(**kwargs)
        context['liste'] = GenreMusical.objects.order_by('nom')
        context['nom'] = 'genremusical'
        context['verbose'] = "genres musicaux"
        return context


class GererStyleMusical(generic.ListView):
    model = StyleMusical
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererStyleMusical, self).get_context_data(**kwargs)
        context['liste'] = StyleMusical.objects.order_by('nom')
        context['nom'] = 'stylemusical'
        context['verbose'] = "style musicaux"
        return context


class GererExperienceMusicale(generic.ListView):
    model = ExperienceMusicale
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererExperienceMusicale, self).get_context_data(**kwargs)
        context['liste'] = ExperienceMusicale.objects.order_by('nom')
        context['nom'] = 'experiencemusicale'
        context['verbose'] = "notions d'expérience musicale"
        return context


class GererContexte(generic.ListView):
    model = Contexte
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererContexte, self).get_context_data(**kwargs)
        context['liste'] = Contexte.objects.order_by('nom')
        context['nom'] = 'contexte'
        context['verbose'] = "contextes"
        return context


class GererRoleEvolution(generic.ListView):
    model = RoleEvolution
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleEvolution, self).get_context_data(**kwargs)
        context['liste'] = RoleEvolution.objects.order_by('nom')
        context['nom'] = 'roleevolution'
        context['verbose'] = "rôle de l'évolution de ..."
        return context


class GererOrganologie(generic.ListView):
    model = Organologie
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererOrganologie, self).get_context_data(**kwargs)
        context['liste'] = Organologie.objects.order_by('nom')
        context['nom'] = 'organologie'
        context['verbose'] = "notions d'organologie"
        return context


class GererSollicitationMusicale(generic.ListView):
    model = SollicitationMusicale
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererSollicitationMusicale, self).get_context_data(**kwargs)
        context['liste'] = SollicitationMusicale.objects.order_by('nom')
        context['nom'] = 'sollicitationmusicale'
        context['verbose'] = "sollicitations musicales"
        return context


class GererSollicitationGenerale(generic.ListView):
    model = SollicitationGenerale
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererSollicitationGenerale, self).get_context_data(**kwargs)
        context['liste'] = SollicitationGenerale.objects.order_by('nom')
        context['nom'] = 'sollicitationgenerale'
        context['verbose'] = "sollicitations generales"
        return context


class GererEvocationGraphique(generic.ListView):
    model = EvocationGraphique
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererEvocationGraphique, self).get_context_data(**kwargs)
        context['liste'] = EvocationGraphique.objects.order_by('nom')
        context['nom'] = 'evocationgraphique'
        context['verbose'] = "évocations graphiques"
        return context


class GererEvocationPlastique(generic.ListView):
    model = EvocationPlastique
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererEvocationPlastique, self).get_context_data(**kwargs)
        context['liste'] = EvocationPlastique.objects.order_by('nom')
        context['nom'] = 'evocationplastique'
        context['verbose'] = "évocations plastiques"
        return context
    

class GererEvocationAutre(generic.ListView):
    model = EvocationAutre
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererEvocationAutre, self).get_context_data(**kwargs)
        context['liste'] = EvocationAutre.objects.order_by('nom')
        context['nom'] = 'evocationautre'
        context['verbose'] = "évocations d'autres disciplines"
        return context


class GererNotionsInter(generic.ListView):
    model = NotionsInter
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererNotionsInter, self).get_context_data(**kwargs)
        context['liste'] = NotionsInter.objects.order_by('nom')
        context['nom'] = 'notionsinter'
        context['verbose'] = "notions évoqués de manière interdisciplinaire"
        return context


class GererRoleFemmes(generic.ListView):
    model = RoleFemmes
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleFemmes, self).get_context_data(**kwargs)
        context['liste'] = RoleFemmes.objects.order_by('nom')
        context['nom'] = 'rolefemmes'
        context['verbose'] = "rôles de femmes"
        return context


class GererRoleHommes(generic.ListView):
    model = RoleHomme
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleHommes, self).get_context_data(**kwargs)
        context['liste'] = RoleHomme.objects.order_by('nom')
        context['nom'] = 'rolehomme'
        context['verbose'] = "rôles d'hommes"
        return context


class GererRoleHumainNeutre(generic.ListView):
    model = RoleHumainNeutre
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleHumainNeutre, self).get_context_data(**kwargs)
        context['liste'] = RoleHumainNeutre.objects.order_by('nom')
        context['nom'] = 'rolehumainneutre'
        context['verbose'] = "rôles d'humains au genre indéterminé"
        return context


class GererRolePersAnimFemmes(generic.ListView):
    model = RolePersAnimFemmes
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRolePersAnimFemmes, self).get_context_data(**kwargs)
        context['liste'] = RolePersAnimFemmes.objects.order_by('nom')
        context['nom'] = 'rolepersanimfemmes'
        context['verbose'] = "rôles des personnage animés au genre féminin"
        return context
    
    
class GererRolePersAnimHommes(generic.ListView):
    model = RolePersAnimHomme
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRolePersAnimHommes, self).get_context_data(**kwargs)
        context['liste'] = RolePersAnimHomme.objects.order_by('nom')
        context['nom'] = 'rolepersanimhomme'
        context['verbose'] = "rôles personnage animés au genre masculin"
        return context


class GererRolePersAnimNeutre(generic.ListView):
    model = RolePersAnimNeutre
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRolePersAnimNeutre, self).get_context_data(**kwargs)
        context['liste'] = RolePersAnimNeutre.objects.order_by('nom')
        context['nom'] = 'rolepersanimneutre'
        context['verbose'] = "rôles personnage animés au genre indéterminé"
        return context


class GererRoleAnimauxFemmes(generic.ListView):
    model = RoleAnimauxFemmes
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleAnimauxFemmes, self).get_context_data(**kwargs)
        context['liste'] = RoleAnimauxFemmes.objects.order_by('nom')
        context['nom'] = 'roleanimauxfemmes'
        context['verbose'] = "rôles animaux au genre féminin"
        return context


class GererRoleAnimauxHommes(generic.ListView):
    model = RoleAnimauxHomme
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleAnimauxHommes, self).get_context_data(**kwargs)
        context['liste'] = RoleAnimauxHomme.objects.order_by('nom')
        context['nom'] = 'roleanimauxhomme'
        context['verbose'] = "rôles animaux au genre masculin"
        return context


class GererRoleAnimauxNeutre(generic.ListView):
    model = RoleAnimauxNeutre
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleAnimauxNeutre, self).get_context_data(**kwargs)
        context['liste'] = RoleAnimauxNeutre.objects.order_by('nom')
        context['nom'] = 'roleanimauxneutre'
        context['verbose'] = "rôles animaux au genre indéterminé"
        return context


class GererRoleInstrFemmes(generic.ListView):
    model = RoleInstrFemmes
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleInstrFemmes, self).get_context_data(**kwargs)
        context['liste'] = RoleInstrFemmes.objects.order_by('nom')
        context['nom'] = 'roleinstrfemmes'
        context['verbose'] = "rôles des instruments animés au genre féminin"
        return context


class GererRoleInstrHommes(generic.ListView):
    model = RoleInstrHomme
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleInstrHommes, self).get_context_data(**kwargs)
        context['liste'] = RoleInstrHomme.objects.order_by('nom')
        context['nom'] = 'rolepersanimhomme'
        context['verbose'] = "rôles des instruments animés au genre masculin"
        return context


class GererRoleInstrNeutre(generic.ListView):
    model = RoleInstrNeutre
    template_name = 'gererX.html'

    def get_context_data(self, **kwargs):
        context = super(GererRoleInstrNeutre, self).get_context_data(**kwargs)
        context['liste'] = RoleInstrNeutre.objects.order_by('nom')
        context['nom'] = 'roleinstrneutre'
        context['verbose'] = "rôles des personnage animés au genre indéterminé"
        return context


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
                   "I.39 Exemples de notions évoquées de façon interdisciplinaires", "STÉ.39.1 Nombre total d'humains","STÉ.39.1 Nombre de femmes", "STÉ.39.1 Nombre d'hommes",
                   "STÉ.39.1 Nombre d'humains au genre indéterminé", "Sté.39.2 Rôle des femmes", "Sté.39.3 Rôle des hommes",
                   "Sté.39.4 Rôle des indeterminés","Sté.40.1 Nombre de personnages animés total","Sté.40.1 Nombre de personnages animés femmes",
                   "Sté.40.1 Nombre de personnages animés hommes", "Sté.40.1 Nombre de personnages animés au genre indéterminé",
                   "Sté.40.3 Rôle des personnages animés féminins", "Sté.40.2 Rôle des personnages animés masculins", "Sté.40.4 Rôle des personnages animés indéterminés",
                   "Sté.41.1 Nombre d'animaux total", "Sté.41.1 Nombre de femelles", "Sté.41.1 Nombre de mâles", "Sté.41.1 Nombre d'animaux au genre indéterminé",
                   "Sté.41.3 Rôle des animaux femelles", "Sté.41.2 Rôle des animaux mâles", "Sté.41.4 Rôle des animaux indéterminés",
                   "Sté.42.1 Nombre d'instruments animés total","Sté.42.1 Nombre d'instruments animés féminins", "Sté.42.1 Nombre d'instruments animés masculins",
                   "Sté.42.1 Nombre d'instruments animés au genre indéterminé", "Sté.42.3 Rôle des instruments anthropomorphes féminins",
                   "Sté.42.2 Rôle des instruments anthropomorphes masculins", "Sté.42.4 Rôle des instruments anthropomorphes neutres",
                   ]

        for col_num in range(len(colones)):
            ws.write(row_num, col_num, colones[col_num], font_style)

        #Construction de listes de liste pour pouvoir manipuler les ManyToMany fields

        loflProdType = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','url','site','ensemble_thematique',
                                                                                                'ensemble_thematique_nom', 'producteur_type__nom'))]
        loflProdNom = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','producteur_nom__nom'))]
        loflSupportDiffusion = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','support_diffusion__nom'))]
        loflFormat = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','format__nom'))]
        loflFormeNarrative = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','forme_narrative__nom','duree','nb_pages','mise_en_ligne_date','depouillement_date','interactivite','materiel_imprimer',
                                                          'personnification_service','commentaire_possible','commentaire_nombre','premier_onglet', 'prem_onglet_autre',
                                                          'deuxieme_onglet', 'deux_onglet_autre', 'troisieme_onglet', 'trois_onglet_autre','plus_de_tois_onglet'))]
        loflModeHebergement = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','mode_hebergement__nom'))]
        loflModeConsultation = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','mode_consultation__nom'))]
        loflLangue = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','narration_langue__nom'))]
        loflSousTitre = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','sous_titre__nom', 'malentendants',
                                                                                                 'malvoyants', 'materiau_musical'))]
        loflOrchestration = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','orchestration__nom'))]
        loflStructure = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','structure__nom'))]
        loflLanguageMusical = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','language_musical__nom'))]
        loflGenreMusical = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','genre_musical__nom'))]
        loflStyleMusical = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','style_musical__nom'))]
        loflExperienceMusical = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','experience_musicale__nom', 
                                                                                                         'elements_socioculturels'))]
        loflEpoque = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','epoque__nom'))]
        loflContexte = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','contexte__nom'))]
        loflRoleEvolution = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','role_evolution__nom'))]
        loflOrganologie = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','organologie__nom'))]
        loflSollicitationMusicale = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','sollicitation_musicale__nom'))]
        loflSollicitationGenerale = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre','sollicitation_generale__nom',
                                                                                                             'temps_mus', 'temps_par', 'temps_mus_par',
                                                                                                             'sonore_valeur'))]
        loflEvocationGraphique = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'evocation_graphique__nom'))]
        loflEvocationPlastique = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'evocation_plastique__nom',
                                                                                                          'evocation_litteraire'))]
        loflEvocationAutre = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'evocation_autre__nom', 'notion_concepts',
                                                                                                      'notion_experiences', 'notion_pratiques'))]
        loflExempleNotionInter = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'exemples_notions_interdisciplinaires__nom', 'nb_humains_total',
                                                                                                  'nb_femmes', 'nb_hommes', 'nb_humains_indetermines'))]
        loflRoleFemme = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_humain_femme__nom'))]
        loflRoleHomme = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_humain_homme__nom'))]
        loflRoleHumainNeutre = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_humain_neutre__nom',
                                                                                                 'nb_pers_anime_total','nb_pers_anime_femmes',
                                                                                                 'nb_pers_anime_hommes', 'nb_pers_anime_indetermines'))]
        loflRolePersAnimFemme = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_pers_anime_femme__nom'))]
        loflRolePersAnimHomme = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_pers_anime_homme__nom'))]
        loflRolePersAnimNeutre = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_pers_anime_neutre__nom', 'nb_animaux_total',
                                                                                                'nb_femelles', 'nb_males', 'nb_animaux_indetermines'))]
        loflRoleFemelle = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_animaux_femme__nom'))]
        loflRoleMale = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_animaux_homme__nom'))]
        loflAnimauxNeutre = [list(elem) for elem in  list(Outil.objects.order_by('titre').values_list('titre','role_animaux_neutre__nom', 'nb_instr_anime_total',
                                                                                                    'nb_instr_anime_femmes','nb_instr_anime_hommes',
                                                                                                    'nb_instr_anime_indetermines'))]
        loflInstrAnimFemme = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_instr_anime_femme__nom'))]
        loflInstrAnimHomme = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_instr_anime_homme__nom'))]
        loflInstrAnimNeutre = [list(elem) for elem in list(Outil.objects.order_by('titre').values_list('titre', 'role_instr_anime_neutre__nom'))]
        
        total = Outil.objects.count()

        loflFin = [None] * total

        #Construction d'une liste de facteurs pour déterminer le nombre d'itération nécéssaire
        facteurs = []
        j = 1
        for i in range(9):
            if i != 0:
                j *= 2
                facteurs.append([i, j])

        nbIter = 0

        # BOUCLES POUR JOINDRE LES "MANYTOMANYFILEDS" DANS UN STRING

        # Type de producteur
        for i in facteurs:
            if ProdType.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflProdType:
                if loflProdType.index(item) != len(loflProdType) - 1:
                    prem = loflProdType[loflProdType.index(item)]
                    deux = loflProdType[loflProdType.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[5] not in deux[5]:
                            prem[5] += ", "
                            prem[5] += deux[5]
                            loflProdType[loflProdType.index(item)] = prem
                            del loflProdType[loflProdType.index(item) + 1]

        # Nom du producteur
        x = ProducteurNom.objects.count()
        for i in facteurs:
            if x < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflProdNom:
                if loflProdNom.index(item) != len(loflProdNom) - 1:
                    prem = loflProdNom[loflProdNom.index(item)]
                    deux = loflProdNom[loflProdNom.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[1] not in deux[1]:
                            prem[1] += ", "
                            prem[1] += deux[1]
                            loflProdNom[loflProdNom.index(item)] = prem
                            del loflProdNom[loflProdNom.index(item) + 1]

        # support de diffusion
        x = SupportDiffusion.objects.count()
        for i in facteurs:
            if x < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflSupportDiffusion:
                if loflSupportDiffusion.index(item) != len(loflSupportDiffusion) - 1:
                    prem = loflSupportDiffusion[loflSupportDiffusion.index(item)]
                    deux = loflSupportDiffusion[loflSupportDiffusion.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[1] not in deux[1]:
                            prem[1] += ", "
                            prem[1] += deux[1]
                            loflSupportDiffusion[loflSupportDiffusion.index(item)] = prem
                            del loflSupportDiffusion[loflSupportDiffusion.index(item) + 1]

        # format
        for i in facteurs:
            if FormatOutil.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(3):
            for item in loflFormat:
                if loflFormat.index(item) != len(loflFormat) - 1:
                    prem = loflFormat[loflFormat.index(item)]
                    Trois = loflFormat[loflFormat.index(item) + 1]
                    if prem[0] == Trois[0]:
                        if prem[1] not in Trois[1]:
                            prem[1] += ", "
                            prem[1] += Trois[1]
                            loflFormat[loflFormat.index(item)] = prem
                            del loflFormat[loflFormat.index(item) + 1]

        # forme narrative
        for i in facteurs:
            if FormeNarrative.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflFormeNarrative:
                if loflFormeNarrative.index(item) != len(loflFormeNarrative) - 1:
                    prem = loflFormeNarrative[loflFormeNarrative.index(item)]
                    Quatre = loflFormeNarrative[loflFormeNarrative.index(item) + 1]
                    if prem[0] == Quatre[0]:
                        if prem[1] not in Quatre[1]:
                            prem[1] += ", "
                            prem[1] += Quatre[1]
                            loflFormeNarrative[loflFormeNarrative.index(item)] = prem
                            del loflFormeNarrative[loflFormeNarrative.index(item) + 1]

        # Mode d'hébergement
        for i in facteurs:
            if ModeHebergement.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflModeHebergement:
                if loflModeHebergement.index(item) != len(loflModeHebergement) - 1:
                    prem = loflModeHebergement[loflModeHebergement.index(item)]
                    Cinq = loflModeHebergement[loflModeHebergement.index(item) + 1]
                    if prem[0] == Cinq[0]:
                        if prem[1] not in Cinq[1]:
                            prem[1] += ", "
                            prem[1] += Cinq[1]
                            loflModeHebergement[loflModeHebergement.index(item)] = prem
                            del loflModeHebergement[loflModeHebergement.index(item) + 1]

        # Mode de consultation
        for i in facteurs:
            if ModeConsultation.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflModeConsultation:
                if loflModeConsultation.index(item) != len(loflModeConsultation) - 1:
                    prem = loflModeConsultation[loflModeConsultation.index(item)]
                    Six = loflModeConsultation[loflModeConsultation.index(item) + 1]
                    if prem[0] == Six[0]:
                        if prem[1] not in Six[1]:
                            prem[1] += ", "
                            prem[1] += Six[1]
                            loflModeConsultation[loflModeConsultation.index(item)] = prem
                            del loflModeConsultation[loflModeConsultation.index(item) + 1]

        # Langue
        for i in facteurs:
            if LangueNarration.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflLangue:
                if loflLangue.index(item) != len(loflLangue) - 1:
                    prem = loflLangue[loflLangue.index(item)]
                    Sept = loflLangue[loflLangue.index(item) + 1]
                    if prem[0] == Sept[0]:
                        if prem[1] not in Sept[1]:
                            prem[1] += ", "
                            prem[1] += Sept[1]
                            loflLangue[loflLangue.index(item)] = prem
                            del loflLangue[loflLangue.index(item) + 1]

        # Sous-titres
        for i in facteurs:
            if SousTitre.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflSousTitre:
                if loflSousTitre.index(item) != len(loflSousTitre) - 1:
                    prem = loflSousTitre[loflSousTitre.index(item)]
                    Huit = loflSousTitre[loflSousTitre.index(item) + 1]
                    if prem[0] == Huit[0]:
                        if prem[1] not in Huit[1]:
                            prem[1] += ", "
                            prem[1] += Huit[1]
                            loflSousTitre[loflSousTitre.index(item)] = prem
                            del loflSousTitre[loflSousTitre.index(item) + 1]

        # Orchestration
        for i in facteurs:
            if Orchestration.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflOrchestration:
                if loflOrchestration.index(item) != len(loflOrchestration) - 1:
                    prem = loflOrchestration[loflOrchestration.index(item)]
                    Neuf = loflOrchestration[loflOrchestration.index(item) + 1]
                    if prem[0] == Neuf[0]:
                        if prem[1] not in Neuf[1]:
                            prem[1] += ", "
                            prem[1] += Neuf[1]
                            loflOrchestration[loflOrchestration.index(item)] = prem
                            del loflOrchestration[loflOrchestration.index(item) + 1]

        # Structure
        for i in facteurs:
            if Structure.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(3):
            for item in loflStructure:
                if loflStructure.index(item) != len(loflStructure) - 1:
                    prem = loflStructure[loflStructure.index(item)]
                    Dix = loflStructure[loflStructure.index(item) + 1]
                    if prem[0] == Dix[0]:
                        if prem[1] not in Dix[1]:
                            prem[1] += ", "
                            prem[1] += Dix[1]
                            loflStructure[loflStructure.index(item)] = prem
                            del loflStructure[loflStructure.index(item) + 1]

        # Language musical
        for i in facteurs:
            if LanguageMusical.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflLanguageMusical:
                if loflLanguageMusical.index(item) != len(loflLanguageMusical) - 1:
                    prem = loflLanguageMusical[loflLanguageMusical.index(item)]
                    Onze = loflLanguageMusical[loflLanguageMusical.index(item) + 1]
                    if prem[0] == Onze[0]:
                        if prem[1] not in Onze[1]:
                            prem[1] += ", "
                            prem[1] += Onze[1]
                            loflLanguageMusical[loflLanguageMusical.index(item)] = prem
                            del loflLanguageMusical[loflLanguageMusical.index(item) + 1]

        # Genre musical
        for i in facteurs:
            if GenreMusical.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflGenreMusical:
                if loflGenreMusical.index(item) != len(loflGenreMusical) - 1:
                    prem = loflGenreMusical[loflGenreMusical.index(item)]
                    Douze = loflGenreMusical[loflGenreMusical.index(item) + 1]
                    if prem[0] == Douze[0]:
                        if prem[1] not in Douze[1]:
                            prem[1] += ", "
                            prem[1] += Douze[1]
                            loflGenreMusical[loflGenreMusical.index(item)] = prem
                            del loflGenreMusical[loflGenreMusical.index(item) + 1]

        # Style musical
        for i in facteurs:
            if StyleMusical.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflStyleMusical:
                if loflStyleMusical.index(item) != len(loflStyleMusical) - 1:
                    prem = loflStyleMusical[loflStyleMusical.index(item)]
                    Treize = loflStyleMusical[loflStyleMusical.index(item) + 1]
                    if prem[0] == Treize[0]:
                        if prem[1] not in Treize[1]:
                            prem[1] += ", "
                            prem[1] += Treize[1]
                            loflStyleMusical[loflStyleMusical.index(item)] = prem
                            del loflStyleMusical[loflStyleMusical.index(item) + 1]

        # Experience Musical
        for i in facteurs:
            if ExperienceMusicale.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflExperienceMusical:
                if loflExperienceMusical.index(item) != len(loflExperienceMusical) - 1:
                    prem = loflExperienceMusical[loflExperienceMusical.index(item)]
                    Quatorze = loflExperienceMusical[loflExperienceMusical.index(item) + 1]
                    if prem[0] == Quatorze[0]:
                        if prem[1] not in Quatorze[1]:
                            prem[1] += ", "
                            prem[1] += Quatorze[1]
                            loflExperienceMusical[loflExperienceMusical.index(item)] = prem
                            del loflExperienceMusical[loflExperienceMusical.index(item) + 1]

        # Époque
        for i in facteurs:
            if Epoque.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflEpoque:
                if loflEpoque.index(item) != len(loflEpoque) - 1:
                    prem = loflEpoque[loflEpoque.index(item)]
                    deux = loflEpoque[loflEpoque.index(item) + 1]
                    if prem[0] == deux[0]:
                        if prem[1] not in deux[1]:
                            prem[1] += ", "
                            prem[1] += deux[1]
                            loflEpoque[loflEpoque.index(item)] = prem
                            del loflEpoque[loflEpoque.index(item) + 1]

        # Contexte
        for i in facteurs:
            if Contexte.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflContexte:
                if loflContexte.index(item) != len(loflContexte) - 1:
                    prem = loflContexte[loflContexte.index(item)]
                    Quinze = loflContexte[loflContexte.index(item) + 1]
                    if prem[0] == Quinze[0]:
                        if prem[1] not in Quinze[1]:
                            prem[1] += ", "
                            prem[1] += Quinze[1]
                            loflContexte[loflContexte.index(item)] = prem
                            del loflContexte[loflContexte.index(item) + 1]

        # Role Evolution
        for i in facteurs:
            if RoleEvolution.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRoleEvolution:
                if loflRoleEvolution.index(item) != len(loflRoleEvolution) - 1:
                    prem = loflRoleEvolution[loflRoleEvolution.index(item)]
                    Seize = loflRoleEvolution[loflRoleEvolution.index(item) + 1]
                    if prem[0] == Seize[0]:
                        if prem[1] not in Seize[1]:
                            prem[1] += ", "
                            prem[1] += Seize[1]
                            loflRoleEvolution[loflRoleEvolution.index(item)] = prem
                            del loflRoleEvolution[loflRoleEvolution.index(item) + 1]

        # Organologie
        for i in facteurs:
            if Orchestration.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflOrganologie:
                if loflOrganologie.index(item) != len(loflOrganologie) - 1:
                    prem = loflOrganologie[loflOrganologie.index(item)]
                    SeizeDeux = loflOrganologie[loflOrganologie.index(item) + 1]
                    if prem[0] == SeizeDeux[0]:
                        if prem[1] not in SeizeDeux[1]:
                            prem[1] += ", "
                            prem[1] += SeizeDeux[1]
                            loflOrganologie[loflOrganologie.index(item)] = prem
                            del loflOrganologie[loflOrganologie.index(item) + 1]

        # Sollicitation musicale
        for i in facteurs:
            if SollicitationMusicale.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflSollicitationMusicale:
                if loflSollicitationMusicale.index(item) != len(loflSollicitationMusicale) - 1:
                    prem = loflSollicitationMusicale[loflSollicitationMusicale.index(item)]
                    DixSept = loflSollicitationMusicale[loflSollicitationMusicale.index(item) + 1]
                    if prem[0] == DixSept[0]:
                        if prem[1] not in DixSept[1]:
                            prem[1] += ", "
                            prem[1] += DixSept[1]
                            loflSollicitationMusicale[loflSollicitationMusicale.index(item)] = prem
                            del loflSollicitationMusicale[loflSollicitationMusicale.index(item) + 1]


        # Sollicitation générale
        for i in facteurs:
            if SollicitationGenerale.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflSollicitationGenerale:
                if loflSollicitationGenerale.index(item) != len(loflSollicitationGenerale) - 1:
                    prem = loflSollicitationGenerale[loflSollicitationGenerale.index(item)]
                    DixHuit = loflSollicitationGenerale[loflSollicitationGenerale.index(item) + 1]
                    if prem[0] == DixHuit[0]:
                        if prem[1] not in DixHuit[1]:
                            prem[1] += ", "
                            prem[1] += DixHuit[1]
                            loflSollicitationGenerale[loflSollicitationGenerale.index(item)] = prem
                            del loflSollicitationGenerale[loflSollicitationGenerale.index(item) + 1]

        # Evocation graphique
        for i in facteurs:
            if EvocationGraphique.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflEvocationGraphique:
                if loflEvocationGraphique.index(item) != len(loflEvocationGraphique) - 1:
                    prem = loflEvocationGraphique[loflEvocationGraphique.index(item)]
                    DixNeuf = loflEvocationGraphique[loflEvocationGraphique.index(item) + 1]
                    if prem[0] == DixNeuf[0]:
                        if prem[1] not in DixNeuf[1]:
                            prem[1] += ", "
                            prem[1] += DixNeuf[1]
                            loflEvocationGraphique[loflEvocationGraphique.index(item)] = prem
                            del loflEvocationGraphique[loflEvocationGraphique.index(item) + 1]

        # Evocation plastique
        for i in facteurs:
            if EvocationPlastique.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflEvocationPlastique:
                if loflEvocationPlastique.index(item) != len(loflEvocationPlastique) - 1:
                    prem = loflEvocationPlastique[loflEvocationPlastique.index(item)]
                    Vingt = loflEvocationPlastique[loflEvocationPlastique.index(item) + 1]
                    if prem[0] == Vingt[0]:
                        if prem[1] not in Vingt[1]:
                            prem[1] += ", "
                            prem[1] += Vingt[1]
                            loflEvocationPlastique[loflEvocationPlastique.index(item)] = prem
                            del loflEvocationPlastique[loflEvocationPlastique.index(item) + 1]

        # Evocation autre
        for i in facteurs:
            if EvocationAutre.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflEvocationAutre:
                if loflEvocationAutre.index(item) != len(loflEvocationAutre) - 1:
                    prem = loflEvocationAutre[loflEvocationAutre.index(item)]
                    VingtEtUn = loflEvocationAutre[loflEvocationAutre.index(item) + 1]
                    if prem[0] == VingtEtUn[0]:
                        if prem[1] not in VingtEtUn[1]:
                            prem[1] += ", "
                            prem[1] += VingtEtUn[1]
                            loflEvocationAutre[loflEvocationAutre.index(item)] = prem
                            del loflEvocationAutre[loflEvocationAutre.index(item) + 1]

        # Exemple notions interdisciplinaires
        for i in facteurs:
            if NotionsInter.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflExempleNotionInter:
                if loflExempleNotionInter.index(item) != len(loflExempleNotionInter) - 1:
                    prem = loflExempleNotionInter[loflExempleNotionInter.index(item)]
                    VingtDeux = loflExempleNotionInter[loflExempleNotionInter.index(item) + 1]
                    if prem[0] == VingtDeux[0]:
                        if prem[1] not in VingtDeux[1]:
                            prem[1] += ", "
                            prem[1] += VingtDeux[1]
                            loflExempleNotionInter[loflExempleNotionInter.index(item)] = prem
                            del loflExempleNotionInter[loflExempleNotionInter.index(item) + 1]

        # Role femme
        for i in facteurs:
            if RoleFemmes.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRoleFemme:
                if loflRoleFemme.index(item) != len(loflRoleFemme) - 1:
                    prem = loflRoleFemme[loflRoleFemme.index(item)]
                    VingtTrois = loflRoleFemme[loflRoleFemme.index(item) + 1]
                    if prem[0] == VingtTrois[0]:
                        if prem[1] not in VingtTrois[1]:
                            prem[1] += ", "
                            prem[1] += VingtTrois[1]
                            loflRoleFemme[loflRoleFemme.index(item)] = prem
                            del loflRoleFemme[loflRoleFemme.index(item) + 1]

        # Role homme
        for i in facteurs:
            if RoleHomme.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRoleHomme:
                if loflRoleHomme.index(item) != len(loflRoleHomme) - 1:
                    prem = loflRoleHomme[loflRoleHomme.index(item)]
                    VingtQuatre = loflRoleHomme[loflRoleHomme.index(item) + 1]
                    if prem[0] == VingtQuatre[0]:
                        if prem[1] not in VingtQuatre[1]:
                            prem[1] += ", "
                            prem[1] += VingtQuatre[1]
                            loflRoleHomme[loflRoleHomme.index(item)] = prem
                            del loflRoleHomme[loflRoleHomme.index(item) + 1]

        # Role humain neutre
        for i in facteurs:
            if RoleHumainNeutre.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRoleHumainNeutre:
                if loflRoleHumainNeutre.index(item) != len(loflRoleHumainNeutre) - 1:
                    prem = loflRoleHumainNeutre[loflRoleHumainNeutre.index(item)]
                    VingtCinq = loflRoleHumainNeutre[loflRoleHumainNeutre.index(item) + 1]
                    if prem[0] == VingtCinq[0]:
                        if prem[1] not in VingtCinq[1]:
                            prem[1] += ", "
                            prem[1] += VingtCinq[1]
                            loflRoleHumainNeutre[loflRoleHumainNeutre.index(item)] = prem
                            del loflRoleHumainNeutre[loflRoleHumainNeutre.index(item) + 1]

        # Role personnage animé femme
        for i in facteurs:
            if RolePersAnimFemmes.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRolePersAnimFemme:
                if loflRolePersAnimFemme.index(item) != len(loflRolePersAnimFemme) - 1:
                    prem = loflRolePersAnimFemme[loflRolePersAnimFemme.index(item)]
                    VingtSix = loflRolePersAnimFemme[loflRolePersAnimFemme.index(item) + 1]
                    if prem[0] == VingtSix[0]:
                        if prem[1] not in VingtSix[1]:
                            prem[1] += ", "
                            prem[1] += VingtSix[1]
                            loflRolePersAnimFemme[loflRolePersAnimFemme.index(item)] = prem
                            del loflRolePersAnimFemme[loflRolePersAnimFemme.index(item) + 1]

        # Role personnage animé homme
        for i in facteurs:
            if RolePersAnimHomme.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRolePersAnimHomme:
                if loflRolePersAnimHomme.index(item) != len(loflRolePersAnimHomme) - 1:
                    prem = loflRolePersAnimHomme[loflRolePersAnimHomme.index(item)]
                    VingtSept = loflRolePersAnimHomme[loflRolePersAnimHomme.index(item) + 1]
                    if prem[0] == VingtSept[0]:
                        if prem[1] not in VingtSept[1]:
                            prem[1] += ", "
                            prem[1] += VingtSept[1]
                            loflRolePersAnimHomme[loflRolePersAnimHomme.index(item)] = prem
                            del loflRolePersAnimHomme[loflRolePersAnimHomme.index(item) + 1]

        # Role presonnage animé neutre
        for i in facteurs:
            if RolePersAnimNeutre.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRolePersAnimNeutre:
                if loflRolePersAnimNeutre.index(item) != len(loflRolePersAnimNeutre) - 1:
                    prem = loflRolePersAnimNeutre[loflRolePersAnimNeutre.index(item)]
                    VingtHuit = loflRolePersAnimNeutre[loflRolePersAnimNeutre.index(item) + 1]
                    if prem[0] == VingtHuit[0]:
                        if prem[1] not in VingtHuit[1]:
                            prem[1] += ", "
                            prem[1] += VingtHuit[1]
                            loflRolePersAnimNeutre[loflRolePersAnimNeutre.index(item)] = prem
                            del loflRolePersAnimNeutre[loflRolePersAnimNeutre.index(item) + 1]

        # Role femelles
        for i in facteurs:
            if RoleAnimauxFemmes.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRoleFemelle:
                if loflRoleFemelle.index(item) != len(loflRoleFemelle) - 1:
                    prem = loflRoleFemelle[loflRoleFemelle.index(item)]
                    VingtNeuf = loflRoleFemelle[loflRoleFemelle.index(item) + 1]
                    if prem[0] == VingtNeuf[0]:
                        if prem[1] not in VingtNeuf[1]:
                            prem[1] += ", "
                            prem[1] += VingtNeuf[1]
                            loflRoleFemelle[loflRoleFemelle.index(item)] = prem
                            del loflRoleFemelle[loflRoleFemelle.index(item) + 1]

        # Rôle mâle
        for i in facteurs:
            if RoleAnimauxHomme.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflRoleMale:
                if loflRoleMale.index(item) != len(loflRoleMale) - 1:
                    prem = loflRoleMale[loflRoleMale.index(item)]
                    Trente = loflRoleMale[loflRoleMale.index(item) + 1]
                    if prem[0] == Trente[0]:
                        if prem[1] not in Trente[1]:
                            prem[1] += ", "
                            prem[1] += Trente[1]
                            loflRoleMale[loflRoleMale.index(item)] = prem
                            del loflRoleMale[loflRoleMale.index(item) + 1]

        # Rôle animaux neutre
        for i in facteurs:
            if RoleAnimauxNeutre.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflAnimauxNeutre:
                if loflAnimauxNeutre.index(item) != len(loflAnimauxNeutre) - 1:
                    prem = loflAnimauxNeutre[loflAnimauxNeutre.index(item)]
                    TrenteEtUn = loflAnimauxNeutre[loflAnimauxNeutre.index(item) + 1]
                    if prem[0] == TrenteEtUn[0]:
                        if prem[1] not in TrenteEtUn[1]:
                            prem[1] += ", "
                            prem[1] += TrenteEtUn[1]
                            loflAnimauxNeutre[loflAnimauxNeutre.index(item)] = prem
                            del loflAnimauxNeutre[loflAnimauxNeutre.index(item) + 1]

        # Rôle intruments femme
        for i in facteurs:
            if RoleInstrFemmes.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflInstrAnimFemme:
                if loflInstrAnimFemme.index(item) != len(loflInstrAnimFemme) - 1:
                    prem = loflInstrAnimFemme[loflInstrAnimFemme.index(item)]
                    TrenteDeux = loflInstrAnimFemme[loflInstrAnimFemme.index(item) + 1]
                    if prem[0] == TrenteDeux[0]:
                        if prem[1] not in TrenteDeux[1]:
                            prem[1] += ", "
                            prem[1] += TrenteDeux[1]
                            loflInstrAnimFemme[loflInstrAnimFemme.index(item)] = prem
                            del loflInstrAnimFemme[loflInstrAnimFemme.index(item) + 1]

        # Rôle instruments homme
        for i in facteurs:
            if RoleInstrHomme.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflInstrAnimHomme:
                if loflInstrAnimHomme.index(item) != len(loflInstrAnimHomme) - 1:
                    prem = loflInstrAnimHomme[loflInstrAnimHomme.index(item)]
                    TrenteTrois = loflInstrAnimHomme[loflInstrAnimHomme.index(item) + 1]
                    if prem[0] == TrenteTrois[0]:
                        if prem[1] not in TrenteTrois[1]:
                            prem[1] += ", "
                            prem[1] += TrenteTrois[1]
                            loflInstrAnimHomme[loflInstrAnimHomme.index(item)] = prem
                            del loflInstrAnimHomme[loflInstrAnimHomme.index(item) + 1]

        # Rôle instruments neutre
        for i in facteurs:
            if RoleInstrNeutre.objects.count() < i[1]:
                nbIter = i[0]
                break

        for i in range(nbIter):
            for item in loflInstrAnimNeutre:
                if loflInstrAnimNeutre.index(item) != len(loflInstrAnimNeutre) - 1:
                    prem = loflInstrAnimNeutre[loflInstrAnimNeutre.index(item)]
                    TrenteQuatre = loflInstrAnimNeutre[loflInstrAnimNeutre.index(item) + 1]
                    if prem[0] == TrenteQuatre[0]:
                        if prem[1] not in TrenteQuatre[1]:
                            prem[1] += ", "
                            prem[1] += TrenteQuatre[1]
                            loflInstrAnimNeutre[loflInstrAnimNeutre.index(item)] = prem
                            del loflInstrAnimNeutre[loflInstrAnimNeutre.index(item) + 1]

        # création d'une liste à envoyer au xls
        for part in range(total):
            del loflProdNom[part][0]
            del loflSupportDiffusion[part][0]
            del loflFormat[part][0]
            del loflFormeNarrative[part][0]
            del loflModeHebergement[part][0]
            del loflModeConsultation[part][0]
            del loflLangue[part][0]
            del loflSousTitre[part][0]
            del loflOrchestration[part][0]
            del loflStructure[part][0]
            del loflLanguageMusical[part][0]
            del loflGenreMusical[part][0]
            del loflStyleMusical[part][0]
            del loflExperienceMusical[part][0]
            del loflEpoque[part][0]
            del loflContexte[part][0]
            del loflRoleEvolution[part][0]
            del loflOrganologie[part][0]
            del loflSollicitationMusicale[part][0]
            del loflSollicitationGenerale[part][0]
            del loflEvocationGraphique[part][0]
            del loflEvocationPlastique[part][0]
            del loflEvocationAutre[part][0]
            del loflExempleNotionInter[part][0]
            del loflRoleFemme[part][0]
            del loflRoleHomme[part][0]
            del loflRoleHumainNeutre[part][0]
            del loflRolePersAnimFemme[part][0]
            del loflRolePersAnimHomme[part][0]
            del loflRolePersAnimNeutre[part][0]
            del loflRoleFemelle[part][0]
            del loflRoleMale[part][0]
            del loflAnimauxNeutre[part][0]
            del loflInstrAnimFemme[part][0]
            del loflInstrAnimHomme[part][0]
            del loflInstrAnimNeutre[part][0]
            loflFin[part] = loflProdType[part] + loflProdNom[part] + loflSupportDiffusion[part] + loflFormat[part] + loflFormeNarrative[part] + loflModeHebergement[part] + loflModeConsultation[part] + loflLangue[part] + loflSousTitre[part]\
                            + loflOrchestration[part] + loflStructure[part] + loflLanguageMusical[part] + loflGenreMusical[part] + loflStyleMusical[part] + loflExperienceMusical[part] + loflEpoque[part] + loflContexte[part] + \
                            loflRoleEvolution[part] + loflOrganologie[part] + loflSollicitationMusicale[part] + loflSollicitationGenerale[part] + loflEvocationGraphique[part] + loflEvocationPlastique[part] + loflEvocationAutre[part] + \
                            loflExempleNotionInter[part] + loflRoleFemme[part] + loflRoleHomme[part] + loflRoleHumainNeutre[part] + loflRolePersAnimFemme[part] + loflRolePersAnimHomme[part] + \
                            loflRolePersAnimNeutre[part] + loflRoleFemelle[part] + loflRoleMale[part] + loflAnimauxNeutre[part] + loflInstrAnimFemme[part] + loflInstrAnimHomme[part] + \
                            loflInstrAnimNeutre[part]

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

    else:
        return redirect('/export_erreur')