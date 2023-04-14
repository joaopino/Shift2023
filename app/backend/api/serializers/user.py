from rest_framework import serializers

from api.serializers.auth_user import GetAuthUserAll, GetAuthUsername
from moelasware.models import Submission, SubmissionAnswer, User


class GetUserUsername(serializers.ModelSerializer):
    user = GetAuthUsername(read_only=True)

    class Meta:
        model = User
        fields = ["user"]


class HallOfFameGetUserInfo(serializers.ModelSerializer):
    user = GetAuthUserAll(read_only=True)
    correct_answers = serializers.SerializerMethodField("get_correct_answers")
    solved_tests = serializers.SerializerMethodField("get_all_solved_tests")

    class Meta:
        model = User
        fields = ["id", "user", "correct_answers", "solved_tests"]

    def get_correct_answers(self, obj):
        return (
            SubmissionAnswer.objects.filter(submission__submitter=obj)
            .filter(answer__correct=True)
            .count()
        )

    def get_all_solved_tests(self, obj):
        return Submission.objects.filter(
            submitter__user__username=obj.user.username
        ).count()
