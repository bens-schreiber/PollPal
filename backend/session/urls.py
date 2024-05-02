from django.urls import path
from .views import *

app_name = "pollpal"

urlpatterns = [
    path("session/", SessionListCreate.as_view(), name="session-list-create"),
    path("session/<int:pk>", SessionDestroy.as_view(), name="session-delete"),
    path("session/start", SessionStart.as_view(), name="session-start"),
    path("question/", QuestionListCreate.as_view(), name="question-list-create"),
    path("session/end", SessionEnd.as_view(), name="session-end"),
]
