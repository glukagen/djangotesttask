from django.conf.urls.defaults import *
from django.conf import settings
import os.path
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^t1_contact/', include('t1_contact.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'base.views.firstpage'),
    (r'^save_person$', 'base.views.save_person'),
    (r'^settings$', 'base.views.settings'),
    (r'^login$', 'base.views.mylogin'),
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    (r'^middleware$', 'base.views.middleware'),
    
)

urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
)
