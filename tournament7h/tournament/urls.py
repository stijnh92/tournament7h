from django.conf.urls import url
from django.contrib import admin
from tournament.views import team as team_view
from tournament.views import player as player_view
from tournament.views import group as group_view
from tournament.views import game as game_view

admin.autodiscover()

urlpatterns = [
    url(r'^teams/$', view=team_view.TeamListView.as_view(), name="team_list"),
    url(r'^teams/(?P<pk>[0-9]+)/$', view=team_view.TeamDetailView.as_view(), name="team_detail"),

    url(r'^players/$',  'tournament.views.player.player_list_view', name="player_list"),
    url(r'^player/(?P<pk>[0-9]+)/$', view=player_view.PlayerDetailView.as_view(), name="player_detail"),

    url(r'^groups/$', view=group_view.GroupListView.as_view(), name="group_list"),
    url(r'^groups/(?P<pk>[0-9]+)/$', view=group_view.GroupDetailView.as_view(), name="group_detail"),

    url(r'^games/$', view=game_view.GameListView.as_view(), name="game_list"),
    url(r'^games/(?P<pk>[0-9]+)/$', view=game_view.GameDetailView.as_view(), name="game_detail"),

    url(r'^game_sheet/(?P<game_id>[0-9]+)/$', 'tournament.views.game.print_sheet', name="game_sheet"),
]
