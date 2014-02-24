from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fiveanimation.views.home', name='home'),
    # url(r'^fiveanimation/', include('fiveanimation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.index'),
    url(r'^animaciones', 'principal.views.animaciones'),
    url(r'^juegos','principal.views.juegos'),
    url(r'^otros','principal.views.otros'),
    url(r'^sobre','principal.views.sobre'),
    url(r'^nuevaApp$','principal.views.nuevaApp'),
    url(r'^nuevoTag$','principal.views.nuevoTag'),
    url(r'^registro$','principal.views.registro'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^cerrar/$', 'principal.views.cerrar'),
    url(r'^runApp/(?P<ide>\d+)$','principal.views.runapp'), 
    url(r'^search/$', 'principal.views.search'),  
)
