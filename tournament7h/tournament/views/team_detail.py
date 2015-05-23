from django.shortcuts import render
from tournament.models import Team


def page(request, pk):
    team = Team.objects.get(id=pk)
    return render(request, 'public/team_detail.html', {'team': team})