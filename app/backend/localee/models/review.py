import datetime

from django.db import models

from moelasware.models import fk
from moelasware.models.quiz import Quiz
from moelasware.models.user import User


class Review(models.Model):
    """
    Represents a Quiz Review.

    It can either be accepted or rejected,
    being a comment mandatory if it is rejected.
    """

    reviewer = fk(User)
    quiz = fk(Quiz)

    creation_date = models.DateField(default=datetime.date.today)
    accepted = models.BooleanField(default=False)
    comment = models.TextField()
    pending = models.BooleanField(default=True)
