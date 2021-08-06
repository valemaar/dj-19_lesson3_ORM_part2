from django.contrib import admin
from django.urls import path
from players.views import list_players_view, list_teams_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', list_players_view, name='players-list'),
    path('teams/', list_teams_view, name='teams-list'),
]
