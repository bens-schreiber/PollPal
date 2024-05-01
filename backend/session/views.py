from rest_framework import generics
from rest_framework.response import Response as _Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.views import View


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDestroy(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionManager(APIView):
    def post(self, request, format=None):
        session_data = request.data.get("session")
        print(session_data)
        question_data = request.data.get("question")

        # Deserialize the data
        session_serializer = SessionSerializer(data=session_data)
        question_serializer = QuestionSerializer(data=question_data)

        session_serializer.is_valid(raise_exception=True)
        question_serializer.is_valid(raise_exception=True)

        question = question_serializer.save()
        session = session_serializer.save()

        poll = Poll.objects.create(session=session, is_accepting_answers=True)

        poll.save()
        question.poll = poll
        question.save()
        return _Response(PollSerializer(poll).data, status=201)
