from django.conf.urls.defaults import *
from django.conf import settings
import os.path
from django.contrib import admin
admin.autodiscover()
from base.models import Location

middleware_data = {
    'queryset': Location.objects.all()[:10],
    'template_name': 'middleware.html'
}

urlpatterns = patterns('',
    # Example:
    # (r'^t1_contact/', include('t1_contact.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'base.views.firstpage'),
    (r'^save_person$', 'base.views.save_person'),
    (r'^settings$', 'base.views.settings'),
    (r'^login$', 'base.views.mylogin'),
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    (r'^middleware$', 'django.views.generic.list_detail.object_list',
        middleware_data),
)

urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
)
