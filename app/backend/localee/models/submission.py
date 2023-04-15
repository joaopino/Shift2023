from django.db import models

from moelasware.models import fk
from moelasware.models.quiz import QuizAnswer
from moelasware.models.test import Test
from moelasware.models.user import User


class Submission(models.Model):
    """
    Represents a Test a user solves.
    When a User solves a test he submits a submission.

    A Submission has several SubmissionAnswer's associated to it,
    where each SubmissionAnswer represents a selected QuizAnswer
    int the Submission.

    For example:
        Quiz: What color is an orange?
            [x] Red
            [ ] Blue
            [x] Orange

        Two SubmissionAnswer's would be created:
            One that has a ForeignKey to the "Red" QuizAnswer
            and another that has a ForeignKey "Orange" QuizAnswer

    """

    test = fk(Test)
    submitter = fk(User)


class SubmissionAnswer(models.Model):
    """
    Represents an Answer made by a User while
    doing a Test.

    For example:
        Quiz: What color is an orange?
            [x] Red
            [ ] Blue
            [x] Orange

        Two SubmissionAnswer's would be created:
            One that has a ForeignKey to the "Red" QuizAnswer
            and another that has a ForeignKey "Orange" QuizAnswer

    """

    submission = fk(Submission)
    answer = fk(QuizAnswer)
