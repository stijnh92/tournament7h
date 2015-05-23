from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    responsible = models.CharField(max_length=40, verbose_name='Team Responsible')
    image = models.ImageField()
    street = models.CharField(max_length=100, verbose_name='Street + Nr.')
    city = models.CharField(max_length=40, verbose_name='City')
    telephone = models.CharField(max_length=15, verbose_name='Telephone Nr.')
    team_id = models.CharField(unique=True, max_length=16)

    def __str__(self):
        return self.name


class Player(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='First Name')
    lastname = models.CharField(max_length=50, verbose_name='Last Name')
    number = models.CharField(max_length=3, verbose_name='Number')
    team = models.ForeignKey(Team, verbose_name="Team")

    def __str__(self):
        return '%s, %s' % (self.lastname, self.firstname)


class Group(models.Model):
    code = models.CharField(max_length=3, verbose_name='Group name')

    def __str__(self):
        return '%s %s' % ('Group', self.code)


class Game(models.Model):
    team_home = models.ForeignKey(Team, related_name='team_home')
    team_away = models.ForeignKey(Team, related_name='team_away')
    group = models.ForeignKey(Group, verbose_name='Group')

    def __str__(self):
        return '%s, %s - %s' % (self.group, self.team_home, self.team_away)


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