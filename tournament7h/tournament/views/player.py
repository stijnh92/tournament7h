from django.views.generic import DetailView
from tournament.models import Player, Team
from django.shortcuts import render


def player_list_view(request):
    players = {}
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for letter in alphabet:
        players.update({
            letter: Player.objects.filter(lastname__startswith=letter).order_by('lastname')
        })

    return render(request, 'public/player_list.html',
                  {
                      'players': players
                  }
                  )


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'public/player_detail.html'
