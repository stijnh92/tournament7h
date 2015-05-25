from django.views.generic import ListView, DetailView
from tournament.models import Group


class GroupListView(ListView):
    model = Group
    template_name = 'public/group_list.html'


class GroupDetailView(DetailView):
    model = Group
    template_name = 'public/group_detail.html'
