from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http.response import HttpResponseBadRequest
from moelasware.models import Quiz, QuizAnswer
from api.serializers import QuizSerializer, QuizAnswerSerializer
from django.db.models import Q
@api_view(["GET"])
@login_required
def get_drafts_view(request):

    user = request.user
    info = Quiz.objects.filter(Q(author__user__username=user, finished = False) | Q(author__user__username=user, rejected = True)).order_by("creation_date")
    
    if not info.exists():
        return JsonResponse({"error":True, "message":"No drafts found"})
        
    quizzes = []
    for i in range(len(info)):
        quizzes.append([info[i].name, info[i].id, info[i].creation_date])

    return JsonResponse({"quizzes": quizzes, "error":False, "message":""}, status=200)


@api_view(["GET"])
@login_required
def get_draft_info_view(request, id):

    author = request.user
    quiz = Quiz.objects.filter(id = id).filter(author__user__username = author)

    if not quiz.exists():
        return HttpResponseBadRequest("Quiz not found")

    quiz = quiz[0]
    answers = QuizAnswer.objects.filter(quiz = quiz).order_by("id")

    if not answers.exists():
        return HttpResponseBadRequest("Answers not found")

    quiz = QuizSerializer(quiz).data

    answers = QuizAnswerSerializer(answers, many = True).data

    count = 1
    for i in answers:
        if i['correct'] == True:
            quiz['correct'] = count
        else:
            count += 1

    return JsonResponse({"draft": [quiz, *answers]})
