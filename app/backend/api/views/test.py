from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from api.serializers import (
    CreateTestSerializer,
    GetTestSerializer,
    GetTestWithSubmissionsSerializer,
)
from api.views import get_n_quizzes_view
from moelasware.models import Test

DEFAULT_TEST_PAGE_LIMIT = 20


@api_view(["GET"])
def get_test_view(request, pk):
    # get test by id -> detail view
    instance = get_object_or_404(Test, pk=pk)
    serializer = GetTestSerializer(instance, many=False)
    return JsonResponse({"test": serializer.data})


# Create a test
@api_view(["POST"])
# TODO: ADD DECORATOR WHEN LOGIN IS IMPLEMENTED
@login_required
def post_test_view(request):
    # TODO: ADD THIS LINE WHEN LOGIN IS IMPLEMENTED
    # author_id = request.user.id
    author_id = 1

    # TODO: Instead of generating the quizzes with get_n_quizzes_view
    # just require having the quizzes in the request.
    # This would require making two API calls
    #   one to generate the quizzes
    #   and another to create the test

    # Required data was all in request (quizzes list was given)
    if "quizzes" in request.data.keys():
        quizzes = request.data.get("quizzes")

    else:
        quizzes_set = get_n_quizzes_view(request)["quizzes"]
        quizzes = quizzes_set.values_list("id", flat=True)

    name = request.data.get("name")
    deserializer_data = {"author": author_id, "name": name, "quizzes": quizzes}
    test_deserializer = CreateTestSerializer(data=deserializer_data)

    if test_deserializer.is_valid(raise_exception=True):
        test = test_deserializer.save()
        response_serializer = GetTestSerializer(test)
        return JsonResponse({"test": response_serializer.data})


@api_view(["GET"])
def get_all_tests_view(request):
    try:
        offset = int(request.query_params.get("offset", default=0))
        limit = int(request.query_params.get("limit", default=DEFAULT_TEST_PAGE_LIMIT))
    except ValueError:
        return HttpResponseBadRequest("Invalid offset and/or limit")

    # TODO: think about actually returning +1 records, for simplifying "Next"-type buttons on frontend
    tests = Test.objects.filter(pk__range=(offset, offset + limit - 1))

    serializer = (
        GetTestWithSubmissionsSerializer
        if request.query_params.get("includeMySubmissions") == "true"
        else GetTestSerializer
    )
    serializer = serializer(tests, many=True)
    return JsonResponse({"tests": serializer.data})


# HIGHLY TEMPORARY SOLUTION!
# TODO: move these to class based views once overall implementation is in better shape
# ~tomasduarte
@api_view(["GET", "POST"])
def tests_view(request):
    proxy = {
        "GET": get_all_tests_view,
        "POST": post_test_view,
    }
    return proxy[request.method](request._request)
