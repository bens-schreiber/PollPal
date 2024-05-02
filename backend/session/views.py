from rest_framework import generics
import rest_framework.response as rf
from .models import *
from .serializers import *
from django.views import View
from rest_framework.views import APIView


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDestroy(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SessionStart(APIView):
    queryset = Session.objects.all()
    serializer_class = SessionStartSerializer

    def post(self, request, format=None):
        """Creates a poll for the session with the provided question and answer."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        poll = serializer.create(serializer.validated_data)

        return rf.Response(PollSerializer(poll).data, status=201)
