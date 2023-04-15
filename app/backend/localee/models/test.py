from django.db import models

from localee.models import fk
from localee.models.quiz import Quiz
from localee.models.user import User


class Test(models.Model):
    """
    A collection of Users.
    """

    author = fk(User)
    quizzes = models.ManyToManyField(Quiz)
    name = models.TextField()
