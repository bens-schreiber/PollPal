from django.urls import path
from .views import SessionDetail
from .views import SessionList

urlpatterns = [
    path('sessions/', SessionList.as_view(), name='session-list'),
    path('sessions/<int:session_id>/', SessionDetail.as_view(), name='session-detail'),
]