from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponseNotFound
from rest_framework.decorators import api_view

from api.serializers import HallOfFameGetTestInfo, HallOfFameGetUserInfo
from moelasware.models import SubmissionAnswer, Test, User


# TODO: this is pretty bad; make use of builtin functions
def return_date(date: str):
    date_months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]
    x = date.replace("T", "-").split("-")
    date_string = date_months[int(x[1]) - 1] + " " + x[2] + " " + x[0]
    return date_string


def handle_serializer_hall_of_fame_view(obj):
    info_list = []

    for i in obj:
        author = i["user"]["username"]
        correct_answers = i["correct_answers"]
        date_joined = return_date(str(i["user"]["date_joined"]))
        solved_tests = i["solved_tests"]
        info_list.append(
            {
                i["id"]: [
                    author,
                    correct_answers,
                    solved_tests,
                    date_joined,
                    i["id"],
                    i["user"]["email"],
                ]
            }
        )

    return info_list


@api_view(["GET"])
@login_required
def hall_of_fame_view(request):

    users = User.objects.all().order_by("user")
    if not users.exists():
        return HttpResponseNotFound("User not found")

    if not SubmissionAnswer.objects.all().exists():
        return HttpResponseNotFound("Submissions not found")

    sub = HallOfFameGetUserInfo(users, many=True).data

    sub = handle_serializer_hall_of_fame_view(sub)

    return JsonResponse({"fame": sub})


def handle_fame_serializer_all_tests(obj):
    obj_list = []
    id = 0

    for i in obj:
        test_id = i["id"]
        test_name = i["name"]
        author = i["author"]["user"]["username"]
        solved_tests = i["solved_tests"]
        tags = ""
        for j in i["quizzes"]:
            for tag in j["tags"]:
                if tag["text"] not in tags:
                    tags += tag["text"]
                    tags += ","

        tags = tags[0 : len(tags) - 1]
        id += 1
        obj_list.append({test_id: [test_id, test_name, solved_tests, tags, author]})

    return obj_list


@api_view(["GET"])
@login_required
def get_fame_all_tests_view(request):

    tests = Test.objects.all().order_by("id")
    if not tests.exists():
        return HttpResponseNotFound("User not found")

    sub = HallOfFameGetTestInfo(tests, many=True).data
    sub = handle_fame_serializer_all_tests(sub)

    return JsonResponse({"submissions_by_test": sub})
