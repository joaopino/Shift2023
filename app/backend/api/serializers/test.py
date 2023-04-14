from rest_framework import serializers

from api.serializers.quiz import QuizSerializer
from api.serializers.user import GetUserUsername
from moelasware.models import Submission, Test


class GetTestSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(read_only=True, many=True)

    class Meta:
        model = Test
        fields = [
            "id",
            "name",
            "author",
            "quizzes",
        ]


class GetTestWithSubmissionsSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(read_only=True, many=True)
    submissions = serializers.PrimaryKeyRelatedField(
        source="submission_set", many=True, read_only=True
    )

    class Meta:
        model = Test
        fields = [
            "id",
            "name",
            "author",
            "quizzes",
            "submissions",
        ]


class CreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["pk", "id", "author", "name", "quizzes"]

    def create(self, validated_data) -> Test:
        quizzes = validated_data.get("quizzes")
        validated_data.pop("quizzes")

        t = Test(**validated_data)
        t.save()
        for quiz in quizzes:
            t.quizzes.add(quiz)

        return t


class GetTestInfo(serializers.ModelSerializer):
    author = GetUserUsername(read_only=True)
    quizzes = QuizSerializer(read_only=True, many=True)

    class Meta:
        model = Test
        fields = ["id", "author", "quizzes", "name"]


class GetTestWithSubmissionsSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(read_only=True, many=True)
    submissions = serializers.PrimaryKeyRelatedField(
        source="submission_set", many=True, read_only=True
    )

    class Meta:
        model = Test
        fields = [
            "id",
            "name",
            "author",
            "quizzes",
            "submissions",
        ]


class HallOfFameGetTestInfo(serializers.ModelSerializer):
    author = GetUserUsername(read_only=True)
    quizzes = QuizSerializer(read_only=True, many=True)
    solved_tests = serializers.SerializerMethodField("get_solved_tests")

    class Meta:
        model = Test
        fields = ["id", "name", "author", "quizzes", "solved_tests"]

    def get_solved_tests(self, obj):
        return Submission.objects.filter(test__id=obj.id).count()
