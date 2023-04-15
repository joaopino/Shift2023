from rest_framework import serializers

from moelasware.models import QuizAnswer


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ["id", "text", "correct", "justification"]
