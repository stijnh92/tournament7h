from django.views.generic import DetailView
from tournament.models import Player, Team
from django.shortcuts import render


def player_list_view(request):
    all_players = Player.objects.all()
    return render(request, 'public/player_list.html',
                  {
                      'players': {'A': all_players, 'B': all_players }
                  }
                  )


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'public/player_detail.html'
