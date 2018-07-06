"""multimedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from bdmultimedia import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alaune', views.AlaUneView.as_view(), name='aLaUne'),
    url(r'^$', views.AlaUneView.as_view(), name='aLaUne'),
    url(r'^liste/$', views.ListeView.as_view(), name = 'liste'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateForm.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteForm.as_view()),
    url(r'^create/$', views.CreateForm.as_view(),name = 'create'),
    url(r'^delete/(?P<pk>\d+)/$', views.OutilDelete.as_view(), name="delete_outil"),
    url('^login/$', auth_views.LoginView.as_view(), name = 'login'),
    url('^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name = 'logout'),
    url('^password_change/$',auth_views.PasswordChangeView.as_view(), name='password_change'),
    url('^password_change/done/$',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^list/$', views.OutilList.as_view(), name='list'),
    url(r'^result(?P<pk>[0-9]+)/$', views.ListDetailView.as_view(), name='list_detail'),
    url(r'^recherche/$', views.SearchForm.as_view(), name = 'recherche'),
    url(r'^recherche_motcle', views.SearchView.as_view(), name= 'recherche_motcle'),
    url(r'^export/xls/$', views.export_xls, name='exporter_xls'),
    url(r'^gerer/', views.GererView.as_view(), name = 'gerer'),
    url(r'^gerer_prodtype/$', views.GererProdType.as_view(), name='gerer_prodType'),
    url(r'^gerer_producteurnom', views.GererProducteurNom.as_view(), name = 'gerer_producteurNom'),
    url(r'^gerer_supportdiffusion/$', views.GererSupportDiffusion.as_view(), name='gerer_supportDiffusion'),
    url(r'^gerer_formenarrative/$', views.GererFormeNarrative.as_view(), name = 'gerer_formeNarrative'),
    url(r'^gerer_formatoutil/$', views.GererFormatOutil.as_view(), name = 'gerer_formatOutil'),
    url(r'^gerer_modehebergement/$', views.GererModeHebergement.as_view(), name = 'gerer_modeHebergement'),
    url(r'^gerer_modeconsultation/$', views.GererModeConsultation.as_view(), name='gerer_modeConsultation'),
    url(r'^gerer_languenarration/$', views.GererLangueNarration.as_view(), name='gerer_langueNarration'),
    url(r'^gerer_soustitre/$',views.GererSousTitre.as_view(),name='gerer_sousTitre'),
    url(r'^gerer_orchestration/$',views.GererOrchestration.as_view(),name='gerer_orchestration'),
    url(r'^gerer_structure/$',views.GererStructure.as_view(),name='gerer_structure'),
    url(r'^gerer_languagemusical/$',views.GererLanguageMusical.as_view(),name='gerer_languageMusical'),
    url(r'^gerer_genremusical/$',views.GererGenreMusical.as_view(),name='gerer_genreMusical'),
    url(r'^gerer_stylemusical/$',views.GererStyleMusical.as_view(),name='gerer_styleMusical'),
    url(r'^gerer_experiencemusicale/$',views.GererExperienceMusicale.as_view(),name='gerer_experienceMusicale'),
    url(r'^gerer_contexte/$',views.GererContexte.as_view(),name='gerer_contexte'),
    url(r'^gerer_roleevolution/$', views.GererRoleEvolution.as_view(),name='gerer_roleEvolution'),
    url(r'^gerer_organologie/$', views.GererOrganologie.as_view(),name='gerer_organologie'),
    url(r'^gerer_sollicitationmusicale/$', views.GererSollicitationMusicale.as_view(),name='gerer_sollicitationMusicale'),
    url(r'^gerer_sollicitationgenerale/$', views.GererSollicitationGenerale.as_view(),name='gerer_sollicitationGenerale'),
    url(r'^gerer_evocationgraphique/$', views.GererEvocationGraphique.as_view(), name='gerer_evocationGraphique'),
    url(r'^gerer_evocationplastique/$', views.GererEvocationPlastique.as_view(), name='gerer_evocationPlastique'),
    url(r'^gerer_evocationautre/$', views.GererEvocationAutre.as_view(), name='gerer_evocationAutre'),
    url(r'^gerer_notionsinter/$', views.GererNotionsInter.as_view(), name='gerer_notionsInter'),
    url(r'^gerer_rolefemmes/$', views.GererRoleFemmes.as_view(), name='gerer_roleFemmes'),
    url(r'^gerer_rolehommes/$', views.GererRoleHommes.as_view(), name='gerer_roleHommes'),
    url(r'^gerer_rolehumainneutre/$', views.GererRoleHumainNeutre.as_view(), name='gerer_roleHumainNeutre'),
    url(r'^gerer_rolepersanimfemmes/$', views.GererRolePersAnimFemmes.as_view(), name='gerer_rolePersAnimFemmes'),
    url(r'^gerer_rolepersanimhommes/$', views.GererRolePersAnimHommes.as_view(), name='gerer_rolePersAnimHommes'),
    url(r'^gerer_rolepersanimneutre/$', views.GererRolePersAnimNeutre.as_view(), name='gerer_rolePersAnimNeutre'),
    url(r'^gerer_roleanimauxfemmes/$', views.GererRoleAnimauxFemmes.as_view(), name = 'gerer_roleAnimauxFemmes'),
    url(r'^gerer_roleanimauxhommes/$', views.GererRoleAnimauxHommes.as_view(), name = 'gerer_roleAnimauxHommes'),
    url(r'^gerer_roleanimauxneutre/$', views.GererRoleAnimauxNeutre.as_view(), name = 'gerer_roleAnimauxNeutre'),
    url(r'^gerer_roleinstrfemmes/$', views.GererRoleInstrFemmes.as_view(), name = 'gerer_roleInstrFemmes'),
    url(r'^gerer_roleinstrhommes/$', views.GererRoleInstrHommes.as_view(), name = 'gerer_roleInstrHommes'),
    url(r'^gerer_roleinstrneutre/$', views.GererRoleInstrNeutre.as_view(), name = 'gerer_roleInstrNeutre'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

