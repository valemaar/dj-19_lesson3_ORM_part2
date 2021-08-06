from django.shortcuts import render

from players.models import Player, Team


def list_players_view(request):
    # players = Player.objects.all()
    players = Player.objects.select_related('team').order_by('id')
    template_name = 'players/list.html'
    context = {
        'players': players,
    }
    return render(request, template_name, context)


def list_teams_view(request):
    teams = Team.objects.prefetch_related(
        'tournaments',
        'sponsors',
    ).order_by('-id')
    template_name = 'players/teams_list.html'
    context = {
        'teams': teams,
    }
    return render(request, template_name, context)
