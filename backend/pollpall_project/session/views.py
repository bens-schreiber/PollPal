from rest_framework import generics
from .models import Session, Question, Response, Poll
from .serializers import SessionSerializer


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = "session_id"


class SessionDestroy(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = "session_id"
