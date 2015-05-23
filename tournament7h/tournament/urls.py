from django.conf.urls import url
from django.contrib import admin
from tournament.views import team as team_view

admin.autodiscover()

urlpatterns = [
    url(r'^teams/$', view=team_view.TeamListView.as_view(), name="team_list"),
    url(r'^teams/(?P<pk>[0-9]+)/$', view=team_view.TeamDetailView.as_view(), name="team_detail"),
]