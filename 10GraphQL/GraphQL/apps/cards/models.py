from django.db import models
from django.utils import timezone
from apps.decks.models import Deck
from apps.utils.models import TimeStamps
from django.utils import timezone
class Card(TimeStamps):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    buckets = (
        (1, "1 day"),
        (2, "2 day"),
        (3, "3 day"),
        (4, "4 day"),
        (5, "5 day"),
    )
    bucket = models.IntegerField(choices=buckets, default=1)

    next_review_at = models.DateTimeField(default=timezone.now())

    next_review_at = models.DateTimeField(default=timezone.now())

    last_reviewed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.question
