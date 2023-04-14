from django.db import models

from moelasware.models import fk


class Tag(models.Model):
    """
    Is associated with a Quiz to display what the Quiz is about
    """

    text = models.TextField()
