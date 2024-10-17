from django.db import models
from apps.utils.models import TimeStamps


# Create your models here.
class Deck(TimeStamps):
    title = models.CharField(max_length=100)

    description = models.TextField()

    last_reviewed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
