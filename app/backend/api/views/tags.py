from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from api.serializers import GetTagSerializer
from moelasware.models import Tag

DEFAULT_TAG_PAGE_LIMIT = 20


@api_view(["GET"])
def get_tag_view(request, pk):

    if pk is not None:
        instance = get_object_or_404(Tag, pk=pk)
        serializer = GetTagSerializer(instance, many=False)

        return JsonResponse({"tag": serializer.data})

    return JsonResponse({"invalid": "not good data"}, status=400)


@api_view(["GET"])
def get_all_tags_view(request):
    try:
        offset = int(request.query_params.get("offset", default=0))
        limit = int(request.query_params.get("limit", default=DEFAULT_TAG_PAGE_LIMIT))
    except ValueError:
        return HttpResponseBadRequest("Invalid offset and/or limit")

    queryset = Tag.objects.filter(pk__range=(offset, offset + limit))

    serializer = GetTagSerializer(queryset, many=True)
    return JsonResponse({"tags": serializer.data})
