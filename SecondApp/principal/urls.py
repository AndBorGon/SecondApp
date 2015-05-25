from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('SecondApp.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^producto','productos',name='producto'),
    url(r'^verproducto','verproducto',name='producto'),
    url(r'^usuario', 'usuarios',name='usuarios'),
    url(r'^recomendacion', 'recomendacion',name='recomendacion'),
    url(r'^verrecomendacion', 'verrecomendacion',name='verrecomendacion'),
    url(r'^addusuario', 'addusuario',name='addusuario'),
    url(r'^index', 'home',name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
