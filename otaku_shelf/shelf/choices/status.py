from django.db import models

class Status(models.TextChoices):
    NOT_STARTED = 'not started'
    WANT_TO_REWATCH = 'want to rewatch'
    NOT_FINISHED = 'not finished'
    IN_PROGRESS = 'in progress'
    DONE = 'done'
