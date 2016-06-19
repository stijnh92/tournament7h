from django.db import models
from operator import itemgetter


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    responsible = models.CharField(max_length=40, verbose_name='Team Responsible')
    image = models.ImageField(blank=True, upload_to='teams/')
    street = models.CharField(max_length=100, verbose_name='Street + Nr.')
    city = models.CharField(max_length=40, verbose_name='City')
    telephone = models.CharField(max_length=15, verbose_name='Telephone Nr.')

    def __str__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='First Name')
    lastname = models.CharField(max_length=50, verbose_name='Last Name')
    number = models.IntegerField(verbose_name='Number')
    team = models.ForeignKey(Team, verbose_name="Team")

    class Meta:
        ordering = ['team', 'number']

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)


class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Location')

    def __str__(self):
        return self.name


class Group(models.Model):
    code = models.CharField(max_length=3, verbose_name='Group name')

    def get_standing(self):
        teams = []
        games = Game.objects.filter(group_id=self.id, finished=True)
        for game in games:
            if game.team_away not in teams:
                teams.append(game.team_away)
            if game.team_home not in teams:
                teams.append(game.team_home)

        standings = []
        for team in teams:
            team_values = {
                'team': team,
                'games_played': 0,
                'games_won': 0,
                'games_lost': 0,
                'games_draw': 0,
                'goals_made': 0,
                'goals_against': 0,
                'goals_ratio': 0,
                'total_points': 0,
            }
            for game in games:
                if game.team_away == team:
                    team_score = game.amount_away
                    opponent_score = game.amount_home
                elif game.team_home == team:
                    team_score = game.amount_home
                    opponent_score = game.amount_away
                else:
                    continue

                if team_score > opponent_score:
                    team_values.update({
                        'games_won': team_values['games_won'] + 1,
                        'total_points': team_values['total_points'] + 3
                    })
                elif team_score < opponent_score:
                    team_values.update({
                        'games_lost': team_values['games_lost'] + 1
                    })
                else:
                    team_values.update({
                        'games_draw': team_values['games_draw'] + 1,
                        'total_points': team_values['total_points'] + 1
                    })

                team_values.update({
                    'games_played': team_values['games_played'] + 1,
                    'goals_made': team_values['goals_made'] + team_score,
                    'goals_against': team_values['goals_against'] + opponent_score,
                    'goals_ratio': team_values['goals_ratio'] + team_score - opponent_score
                })

            standings.append(team_values)

        sorted_standings = sorted(standings, key=itemgetter('total_points', 'games_won', 'goals_ratio'), reverse=True)
        return sorted_standings

    def __str__(self):
        return '%s %s' % ('Group', self.code)


class Game(models.Model):
    team_home = models.ForeignKey(Team, related_name='team_home')
    team_away = models.ForeignKey(Team, related_name='team_away')
    amount_home = models.IntegerField(verbose_name='Score Home')
    amount_away = models.IntegerField(verbose_name='Score Away')
    group = models.ForeignKey(Group, verbose_name='Group')
    location = models.ForeignKey(Location, verbose_name='Location', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Date', blank=True)
    finished = models.BooleanField(verbose_name='Finished')

    def __str__(self):
        return '%s, %s - %s' % (self.group, self.team_home, self.team_away)

    class Meta:
        ordering = ['date', 'group']


class Goal(models.Model):
    player = models.ForeignKey(Player, verbose_name='Player')
    game = models.ForeignKey(Game, verbose_name='Game')
    amount = models.IntegerField()

    def __str__(self):
        return '%s, %d goals' % (self.player, self.amount)


class FairPlay(models.Model):
    team = models.ForeignKey(Team, verbose_name='Team')
    game = models.ForeignKey(Game, verbose_name='Game')
    amount = models.IntegerField()

    def __str__(self):
        return '%s, %d/10' % (self.team, self.amount)
