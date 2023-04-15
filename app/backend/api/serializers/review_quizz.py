from rest_framework import serializers

from api.serializers.quiz import QuizInfoSerializer
from api.serializers.tag import GetTagSerializer
from api.serializers.user import GetUserUsername
from moelasware.models.quiz import Quiz, QuizAnswer
from moelasware.models.review import Review


class GetQuizReviewSerializer(serializers.ModelSerializer):
    tags = GetTagSerializer(read_only=True, many=True)
    author = GetUserUsername(read_only=True)

    class Meta:
        model = Quiz
        fields = [
            "id",
            "name",
            "author",
            "tags",
            "question",
            "description",
            "creation_date",
        ]


class GetQuizReviewNewSerializer(serializers.ModelSerializer):
    reviewer = GetUserUsername(read_only=True)
    review_result = serializers.SerializerMethodField("get_review_result")

    class Meta:
        model = Review
        fields = ["id", "reviewer", "creation_date", "comment", "review_result"]

    def get_review_result(self, obj):

        if Review.objects.filter(id=obj.id).filter(accepted=False):
            return "rejected"

        else:
            return "accepted"


class GetQuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ["id", "text", "correct", "justification"]


class GetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "comment", "quiz", "reviewer"]


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["reviewer", "quiz", "accepted", "comment"]


class QuizReviewSerializer(serializers.ModelSerializer):
    tags = GetTagSerializer(read_only=True, many=True)
    author = GetUserUsername(read_only=True)
    review_count = serializers.SerializerMethodField("get_review_count")

    class Meta:
        model = Quiz
        fields = ["id", "name", "tags", "author", "review_count", "creation_date"]

    def get_review_count(self, obj):
        return Review.objects.filter(quiz=obj, pending=True).count()
