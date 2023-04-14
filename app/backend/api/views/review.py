from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from api.serializers import (
    CreateReviewSerializer,
    CreateTestSerializer,
    GetQuizAnswerSerializer,
    GetQuizReviewSerializer,
    GetReviewSerializer,
    GetTestSerializer,
    QuizSerializer,
    QuizReviewSerializer,
)
from moelasware.models import (
    Quiz,
    QuizAnswer,
    Review,
    Submission,
    SubmissionAnswer,
    Tag,
    Test,
    User,
)


@api_view(["GET"])
@login_required
def get_info_review_view(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)

    quiz_serializer = GetQuizReviewSerializer(quiz)
    answers = QuizAnswer.objects.filter(quiz=quiz.id)
    answer_serializer = GetQuizAnswerSerializer(answers, many=True)
    return JsonResponse({"quiz": quiz_serializer.data, "answers": answer_serializer.data})

@api_view(["GET"])
@login_required
def get_info_quiz_view(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)
    answers = QuizAnswer.objects.filter(quiz=quiz.id)

    quiz = GetQuizReviewSerializer(quiz).data

    obj_list = [quiz["id"], quiz["name"],quiz["author"]["user"]["username"], quiz["tags"][0]["text"], quiz["question"], quiz["description"], quiz["creation_date"]]
    
    answer_serializer = GetQuizAnswerSerializer(answers, many=True).data

    answer_list = []
    for i in answer_serializer:
        answer_list.append([i['text'], i['justification'], i['correct']])

    return JsonResponse({"quiz": obj_list, "answers": answer_list})



@api_view(["POST"])
@login_required
def create_review_view(request):

    data = request.data['args']
    user = User.objects.filter(user__username = request.user)

    if not user.exists():
        return HttpResponseBadRequest("User not found")

    user = user[0]

    data["reviewer"] = user.id
    serializer = CreateReviewSerializer(data=data)

    # raises exception on why its not valid
    if serializer.is_valid(raise_exception=True):
        serializer = serializer.data
        review = Review.objects.filter(quiz__id=data['quiz']).filter(reviewer__id = serializer['reviewer'])
        review = review[0]

        review.pending = False
        review.accepted = serializer["accepted"]


        if not review.accepted:
            review.quiz.approved = False
            review.quiz.rejected = True

        if Review.objects.filter(quiz = review.quiz).filter(accepted = True).filter(pending = False).count() == 3:
            review.quiz.approved = True
            

        review.comment = serializer["comment"]
        review.save()
        review.quiz.save()
        return JsonResponse(serializer)

    return JsonResponse({"error": "Bad data"})


def quiz_review_serializer_handler(data):
    data_list = []
    for i in data:
        data_list.append([i['id'],i['name'],i['tags'][0]['text'],i['author']['user']['username'], i['review_count'], i['creation_date']])
    return data_list

@api_view(["GET"])
@login_required
def get_quizzes_of_a_reviewer_view(request):

    reviewer = Review.objects.filter(reviewer__user__username=request.user).filter(pending=True)

    if not reviewer.exists():
        return JsonResponse({"error": True, "message": "Reviews not found"})
        #return HttpResponseBadRequest("Reviews not found")

    reviewer_list = []
    for i in reviewer:
        reviewer_list.append(QuizReviewSerializer(i.quiz).data)

    reviewer_list = quiz_review_serializer_handler(reviewer_list)

    return JsonResponse({"error": False, "message":"", "info": reviewer_list})


@api_view(["GET"])
@login_required
def get_quiz_info_review_view(request, id):

    chosen_quiz = get_object_or_404(Review, id=id)
    serializer = GetReviewSerializer(chosen_quiz).data
    return JsonResponse({"reviewer": serializer})


@api_view(["GET"])
@login_required
def get_if_has_done_quiz_view(request):
    
    user = User.objects.filter(user__username=request.user)

    if not user.exists():
        return HttpResponseBadRequest("User not found")

    user = user[0]

    quiz = Quiz.objects.filter(author=user)

    validated = 0

    if quiz.exists():
        validated = 1

    return JsonResponse({"valid": validated})
