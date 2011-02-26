from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wsl/', include('wsl.foo.urls')),
    (r'^$', 'wsl.home.views.index'),
    (r'^minicurso/(?P<mc>.*)$', 'wsl.programacao.views.minicurso'),
    (r'^palestrante/(?P<palestrante>.*)$', 'wsl.programacao.views.palestrante'),
	(r'^programacao/', include('wsl.programacao.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.WSL_SRC_ROOT + "static"}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
