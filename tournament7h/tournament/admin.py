from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tournament.models import Player, Team, Group, Game, Goal, FairPlay

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Group)
admin.site.register(Game)
admin.site.register(Goal)
admin.site.register(FairPlay)