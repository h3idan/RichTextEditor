from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^upload/', 'DjangoCkeditor.views.upload', name='ckeditor_upload'),
    url(r'^browse/', 'DjangoCkeditor.views.browse', name='ckeditor_browse'),
)
