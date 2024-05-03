from django.urls import path
from .views import *

app_name = "pollpal"

urlpatterns = [
    path("session/", SessionListCreate.as_view(), name="session-list-create"),
    path("session/<int:pk>", SessionDestroy.as_view(), name="session-delete"),
    path("session/start", SessionStart.as_view(), name="session-start"),
    # path("question/", QuestionListCreate.as_view(), name="question-list-create"),
    path("session/<int:session_id>/end", SessionEnd.as_view(), name="session-end"),
    path("poll/next-question", PollNextQuestion.as_view(), name="poll-next-question"),
    path(
        "poll/set-accepting-answer",
        PollSetAcceptingAnswers.as_view(),
        name="poll-set-accepting-answer",
    ),
    path(
        "poll/<int:poll_id>/answer",
        PollGetAnswer.as_view(),
        name="poll-get-correct-answer",
    ),
    path(
        "poll/submit-response",
        PollSubmitResponse.as_view(),
        name="poll-submit-response",
    ),
    path(
        "question/create",
        QuestionCreate.as_view(),
        name="question-create",
    ),
    path("question/<int:question_id>/answer", AnswerList.as_view(), name="answer-list"),
]
