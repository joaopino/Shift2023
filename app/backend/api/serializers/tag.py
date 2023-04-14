from rest_framework import serializers

from moelasware.models import Tag


class GetTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["text"]
