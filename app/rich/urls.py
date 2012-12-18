#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2012-12-18 10:37
#**********************************


from django.conf.urls import patterns, include, url
from rich import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rich.views.home', name='home'),
    # url(r'^rich/', include('rich.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^ckeditor/', include('DjangoCkeditor.urls'))

)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

)
