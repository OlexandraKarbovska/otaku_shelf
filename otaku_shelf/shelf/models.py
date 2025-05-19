from django.db import models
from .choices.score import Score
from .choices.status import Status
from .choices.genre import Genre

class ListOfTitles(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Title(models.Model):
    list_of_titles = models.ForeignKey(ListOfTitles, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, choices=Genre)
    status = models.CharField(max_length=100, choices=Status)
    score = models.IntegerField(choices=Score)
