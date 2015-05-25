# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FairPlay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_home', models.IntegerField(verbose_name=b'Score Home')),
                ('amount_away', models.IntegerField(verbose_name=b'Score Away')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('game', models.ForeignKey(verbose_name=b'Game', to='tournament.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=3, verbose_name=b'Group name')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=50, verbose_name=b'First Name')),
                ('lastname', models.CharField(max_length=50, verbose_name=b'Last Name')),
                ('number', models.CharField(max_length=3, verbose_name=b'Number')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('responsible', models.CharField(max_length=40, verbose_name=b'Team Responsible')),
                ('image', models.ImageField(upload_to=b'', blank=True)),
                ('street', models.CharField(max_length=100, verbose_name=b'Street + Nr.')),
                ('city', models.CharField(max_length=40, verbose_name=b'City')),
                ('telephone', models.CharField(max_length=15, verbose_name=b'Telephone Nr.')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', to='tournament.Team'),
        ),
        migrations.AddField(
            model_name='goal',
            name='player',
            field=models.ForeignKey(verbose_name=b'Player', to='tournament.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='group',
            field=models.ForeignKey(verbose_name=b'Group', to='tournament.Group'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_away',
            field=models.ForeignKey(related_name='team_away', to='tournament.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_home',
            field=models.ForeignKey(related_name='team_home', to='tournament.Team'),
        ),
        migrations.AddField(
            model_name='fairplay',
            name='game',
            field=models.ForeignKey(verbose_name=b'Game', to='tournament.Game'),
        ),
        migrations.AddField(
            model_name='fairplay',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', to='tournament.Team'),
        ),
    ]
