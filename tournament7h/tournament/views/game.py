from django.views.generic import ListView, DetailView
from tournament.models import Game


class GameListView(ListView):
    model = Game
    template_name = 'public/game_list.html'


class GameDetailView(DetailView):
    model = Game
    template_name = 'public/game_detail.html'
