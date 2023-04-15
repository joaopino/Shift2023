from rest_framework import serializers


class CreateEditQuizSerializer(serializers.Serializer):
    class Meta:
        fields = [
            "id",
            "author_id",
            "text",
            "description",
            "question",
            "answer",
            "name",
            "aproved",
            "tags",
            "reviews",
            "finished",
            "creation_date",
        ]
