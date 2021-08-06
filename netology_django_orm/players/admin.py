from django.contrib import admin

from players.models import Player, Team, Sponsor, Sponsorship, Tournament


class SponsorshipInline(admin.TabularInline):
    model = Sponsorship


class PlayerAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    inlines = [
        SponsorshipInline
    ]


class SponsorAdmin(admin.ModelAdmin):
    inlines = [
        SponsorshipInline
    ]


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Tournament, TournamentAdmin)
