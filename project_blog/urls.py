from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blogApp.models import Artigo

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index',
		{'queryset': Artigo.objects.all(),
		'date_field': 'publicacao'}),
	url(r'^admin/', include(admin.site.urls)),
	(r'^artigo/(?P<artigo_id>\d+)/$', 'blogApp.views.artigo'),

	(r'^contato/$', 'views.contato'),
	(r'^comments/', include('django.contrib.comments.urls')),
)

if settings.LOCAL:
	urlpatterns += patterns('',
		(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
	)


