from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'SecondApp.views.home', name='home'),
    # url(r'^SecondApp/', include('SecondApp.foo.urls')),
    url(r'^usuario', 'SecondApp.views.usuarios',name='usuarios'),
    url(r'^recomendacion', 'SecondApp.views.recomendacion',name='recomendacion'),
    url(r'^verrecomendacion', 'SecondApp.views.verrecomendacion',name='verrecomendacion'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
