from django.shortcuts import render

from players.models import Player


def list_players_view(request):

    # players = Player.objects.all()

    players = Player.objects.select_related('team').all()

    template_name = 'players/list.html'
    context = {
        'players': players,
    }
    return render(request, template_name, context)
