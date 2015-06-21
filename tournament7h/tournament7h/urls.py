from django.conf.urls import include, url
from django.contrib import admin
from . import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', 'tournament.views.index.page', name="public_index"),
    url(r'^team-detail-(?P<pk>\d+)$', 'tournament.views.team_detail.page', name="team_detail"),
    url(r'^create-team$', 'tournament.views.create_team.page', name="create_team"),
    url(r'^connection/$', 'tournament.views.connections.page', name="public_connection"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tournament/', include('tournament.urls', namespace='tournament')),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ]
