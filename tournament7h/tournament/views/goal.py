from django.shortcuts import render
from django.db.models import Sum

from tournament.models import Goal, Player


def top_scorers_view(request):
    scorers = Goal.objects.values('player_id').annotate(sum_goals=Sum('amount')).order_by('-sum_goals')

    for scorer in scorers:
        scorer.update({
            'player': Player.objects.get(pk=scorer['player_id'])
        })

    values = {
        'top_scorers': scorers
    }
    return render(request, 'public/top_scorers_list.html', values)
