import datetime

from django.db import models

from moelasware.models import fk
from moelasware.models.tag import Tag
from moelasware.models.user import User


# I really dislike how you cannot do this in a tidy way in Python because inner classes cannot
# reference other inner classes... oh well
class QuizQuerySet(models.QuerySet):
    def can_be_added_to_a_test(self):
        # here to avoid circular imports;
        # this is cached anyways, so it isn't a performance hazard
        from moelasware.models.test import Test

        return self.filter(approved=True).filter(
            ~models.Exists(Test.objects.filter(quizzes__id=models.OuterRef("id")))
        )


class QuizManager(models.Manager):
    def get_queryset(self):
        return QuizQuerySet(self.model)

    def can_be_added_to_a_test(self):
        print(self.get_queryset().can_be_added_to_a_test().query)
        return self.get_queryset().can_be_added_to_a_test()


class Quiz(models.Model):
    """
    Question that has several answers and associated tags.
    """

    author = fk(User)
    tags = models.ManyToManyField(Tag)

    name = models.TextField()
    question = models.TextField()
    description = models.TextField()
    finished = models.BooleanField(default=False)

    creation_date = models.DateField(default=datetime.date.today)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    review_count = models.IntegerField(default=0)

    objects = QuizManager()

    def can_be_added_to_a_test(self):
        return self.test_set.count() < 2


class QuizAnswer(models.Model):
    """
    Represents an answer in a Quiz.

    For example:

        Quiz: What color is an orange?
            [ ] Red
            [ ] Blue
            [ ] Orange (correct)

    Here, there are three QuizAnswer's
        Red,
        Blue,
        and Orange

    and only Orange is correct.

    Every QuizAnswer needs to justify why
    it is or isn't correct.
    """

    quiz = fk(Quiz)

    text = models.TextField()
    correct = models.BooleanField(default=False)
    justification = models.TextField()
