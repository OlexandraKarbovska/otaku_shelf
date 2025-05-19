from django.db import models

class Genre(models.TextChoices):
    COMEDY = 'comedy'
    HORROR = 'horror'
    MYSTERY = 'mystery'
    HISTORICAL = 'historical'
    PSYCHOLOGICAL = 'psychological'
    SHOUNEN = 'shounen'
    SHOUJO = 'shoujo'
    ART = 'art'
    SPORT = 'sport'
    ROMANTIC = 'romantic'
