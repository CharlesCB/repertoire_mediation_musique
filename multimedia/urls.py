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
    url(r'^$', views.HomeView.as_view(), name = 'home'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/', views.CreateForm.as_view(), name = 'create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateForm.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteForm.as_view()),
   # url('^', include('django.contrib.auth.urls')),
    url('^login/$', auth_views.LoginView.as_view(), name = 'login'),
    url('^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
    url('^password_change/$',auth_views.PasswordChangeView.as_view(), name='password_change'),
    url('^password_change/done/$',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^elemmus-autocomplete/$', views.ElemMusAutocomplete.as_view(), name='elemmus-autocomplete', ),
    url(r'^export/xls/$', views.export_xls, name='exporter_outils'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

