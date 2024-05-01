from django.urls import path
from .views import SessionDestroy, SessionListCreate

app_name = "pollpal"

urlpatterns = [
    path("session/", SessionListCreate.as_view(), name="session-list-create"),
    path("session/<int:pk>", SessionDestroy.as_view(), name="session-delete"),
]
