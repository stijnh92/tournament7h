from django.views.generic import ListView, DetailView
from tournament.models import Team


class TeamListView(ListView):
    model = Team
    template_name = 'public/team_list.html'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'public/team_detail.html'
