from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

urlpatterns = [
    # TESTS
    path("tests/<int:pk>/", views.get_test_view),
    path("tests/", views.tests_view),
    path("tests/<int:pk>/submissions/", views.submission_view),
    path("tags/<int:pk>/", views.get_tag_view),
    path("tags/", views.get_all_tags_view),
    path("user/can_create/test/", views.can_create_test_view),
    # QUIZZES
    path("quizzes/gen/", views.get_n_quizzes_view),
    path("quizzes/<int:quiz_id>/answers/", views.get_answers_for_quiz_view),
    path("quizzes/count/", views.get_total_number_of_quizzes_view),
    # CREATE QUIZ
    path("quizzes/", views.create_quiz_view),
    path("quizzes/<int:id>/", views.edit_quiz_view),
    path("quizz/<int:pk>/", views.get_quiz_view),
    path("quiz/<int:pk>/info/", views.get_info_quiz_view),
    path("myquizzes/", views.get_user_quizzes_view),
    path("quiz/<int:id>/reviews/", views.get_reviews_of_a_quiz_view),
    # EDIT DRAFT
    path("drafts/", views.get_drafts_view),
    path("draft/<int:id>/", views.get_draft_info_view),
    # REVIEWS
    path("review/quiz/<int:pk>/", views.get_info_review_view),
    path("review/create/", views.create_review_view),
    path("review/quizzes/", views.get_quizzes_of_a_reviewer_view),
    path("review/validate/", views.get_if_has_done_quiz_view),
    # path("review/quiz/<int:id>/", views.get_quiz_info_review_view),
    # HALL OF FAME
    path("fame/users/", views.hall_of_fame_view),
    path("fame/users/<int:pk>/submissions/", views.submissions_by_user_view),
    path("fame/tests/<int:pk>/submissions/", views.submission_of_a_test_view),
    path("fame/tests/", views.get_fame_all_tests_view),
    # PROFILE
    path("profile/", views.profile_view),
    # LOGIN/REGISTER
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("register/", views.register_view),
    path("quiz/import/", views.import_xml),
    path("quiz/export/", views.export_xml),
]
