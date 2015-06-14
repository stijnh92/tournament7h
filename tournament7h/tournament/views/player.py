from django.views.generic import ListView, DetailView
from tournament.models import Player


class PlayerListView(ListView):
    model = Player
    template_name = 'public/player_list.html'


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'public/player_detail.html'
