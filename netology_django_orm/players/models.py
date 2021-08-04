from django.db import models


class Player(models.Model):
    name = models.TextField(db_index=True)
    # name = models.TextField(db_index=True)  # создать индекс => db_index=True
    team = models.ForeignKey(  # team_id
        'Team',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.id}: {self.name}'


class Team(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.name}'


class Tournament(models.Model):
    name = models.TextField()
    teams = models.ManyToManyField(Team, related_name='tournaments')

    def __str__(self):
        return f'{self.id}: {self.name}'
