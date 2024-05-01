from django.urls import path
from .views import *

app_name = "pollpal"

urlpatterns = [
    path("session/", SessionListCreate.as_view(), name="session-list-create"),
    path("session/<int:pk>", SessionDestroy.as_view(), name="session-delete"),
    path("session/manager", SessionManager.as_view(), name="session-manage"),
]
