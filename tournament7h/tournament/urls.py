from django.conf.urls import url
from django.contrib import admin
from tournament.views import team as team_view
from tournament.views import group as group_view
from tournament.views import game as game_view

admin.autodiscover()

urlpatterns = [
    url(r'^teams/$', view=team_view.TeamListView.as_view(), name="team_list"),
    url(r'^teams/(?P<pk>[0-9]+)/$', view=team_view.TeamDetailView.as_view(), name="team_detail"),

    url(r'^groups/(?P<pk>[0-9]+)/$', view=group_view.GroupDetailView.as_view(), name="group_detail"),

    url(r'^games/$', view=game_view.GameListView.as_view(), name="game_list"),
    url(r'^games/(?P<pk>[0-9]+)/$', view=game_view.GameDetailView.as_view(), name="game_detail"),

]
