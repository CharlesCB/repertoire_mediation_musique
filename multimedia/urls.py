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
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateForm.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteForm.as_view()),

    url(r'^delete/(?P<pk>\d+)/$', views.OutilDelete.as_view(), name="delete_outil"),

    url('^login/$', auth_views.LoginView.as_view(), name = 'login'),
    url('^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'}, name = 'logout'),
    url('^password_change/$',auth_views.PasswordChangeView.as_view(), name='password_change'),
    url('^password_change/done/$',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^list/$', views.OutilList.as_view(), name='list'),
    url(r'^result(?P<pk>[0-9]+)/$', views.ListDetailView.as_view(), name='list_detail'),
    url(r'^search/$', views.SearchForm.as_view(), name = 'search'),
    url(r'^export/xls/$', views.export_xls, name='exporter_xls'),
    #url(r'^export/csv/$', views.export_csv, name='exporter_csv'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

