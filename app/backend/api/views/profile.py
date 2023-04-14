from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view

from api.serializers import *
from moelasware.models import *


@api_view(["GET"])
@login_required
def profile_view(request):

    user = User.objects.filter(user__username=request.user)

    if not user.exists():
        return JsonResponse(
            {"user": user.user.username, "error": True, "message": "User not found"}
        )

    user = user[0]

    tests_done = Submission.objects.filter(submitter=user)

    if not tests_done.exists():
        return JsonResponse(
            {"user": user.user.username, "error": True, "message": "No tests found"}
        )

    correct_answers = SubmissionAnswer.objects.filter(answer__correct=True).filter(
        submission__submitter=user
    )
    number_of_correct_answers = correct_answers.count()
    if not number_of_correct_answers:
        return JsonResponse(
            {"user": user.user.username, "error": True, "message": "No correct answers"}
        )

    tags = {}
    for i in Tag.objects.all():
        tags[i.text] = 0

    for i in correct_answers:
        for j in i.answer.quiz.tags.all():
            tags[j.text] += 1

    return JsonResponse(
        {
            "profile": tags,
            "correct_answers": number_of_correct_answers,
            "user": user.user.username,
        }
    )
