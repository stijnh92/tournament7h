from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tournament.models import Player, Team, Group, Game, Goal, FairPlay, Location

class GoalInline(admin.TabularInline):
    model = Goal
    classes = ('grp-collapse grp-closed',)

class FairPlayInline(admin.TabularInline):
    model = FairPlay
    classes = ('grp-collapse grp-closed',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'group', 'team_home', 'team_away', 'amount_home', 'amount_away')
    list_filter = ('group', 'team_home', 'team_away')
    inlines = [
        GoalInline, FairPlayInline
    ]




admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Group)
admin.site.register(Goal)
admin.site.register(FairPlay)
admin.site.register(Location)