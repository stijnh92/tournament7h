from django.shortcuts import render
from tournament.models import Team


def page(request):
    all_teams = Team.objects.all()
    return render(request, 'public/index.html',
                  {
                      'teams': all_teams}
                  )