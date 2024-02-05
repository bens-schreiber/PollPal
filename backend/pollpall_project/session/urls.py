from django.urls import path
from .views import SessionView

urlpatterns = [
    path('sessions/', SessionView.as_view(), name='session-list'),
    path('sessions/<int:session_id>/', SessionView.as_view(), name='session-detail'),
]
