from django.shortcuts import get_object_or_404
from rest_framework import generics
import rest_framework.response as rf
from .models import *
from .serializers import *
from django.views import View
from rest_framework.views import APIView
from django.http import HttpResponseBadRequest


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDestroy(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class QuestionCreate(APIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer

    def post(self, request, format=None):
        """Creates a question with the provided prompt and answers."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.are_answers_valid(serializer.validated_data["answers"])

        question = serializer.create(serializer.validated_data)

        return rf.Response(QuestionSerializer(question).data, status=201)


class SessionStart(APIView):
    queryset = Session.objects.all()
    serializer_class = SessionStartSerializer

    def post(self, request, format=None):
        """Creates a poll for the session with the provided question and answer."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        poll = serializer.create(serializer.validated_data)

        return rf.Response(PollSerializer(poll).data, status=201)


class SessionEnd(APIView):
    queryset = Session.objects.all()

    def delete(self, request, session_id, format=None):
        """Deletes a Poll from a session. If there is no Poll, return 400. If the poll is accepting answers, return 400."""

        session: Session = get_object_or_404(Session, pk=session_id)

        if not (Poll.objects.filter(session=session).exists()):
            return HttpResponseBadRequest("Poll does not exist.")

        poll: Poll = session.poll

        if poll.is_accepting_answers:
            return HttpResponseBadRequest("Poll is accepting answers.")

        poll.delete()

        return rf.Response(status=202)


class PollNextQuestion(APIView):
    queryset = Poll.objects.all()
    serializer_class = PollNextQuestionSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.is_poll_valid()

        poll: Poll = serializer.create(serializer.validated_data)

        new_question: Question = serializer.validated_data.pop("question")
        Question.objects.filter(poll=poll).first().delete()

        new_question.poll = poll
        new_question.save()

        return rf.Response(PollSerializer(poll).data, status=200)


class PollSetAcceptingAnswers(APIView):
    queryset = Poll.objects.all()
    serializer_class = PollSetAcceptingAnswersSerializer

    def patch(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.is_poll_valid()

        poll: Poll = serializer.create(serializer.validated_data)
        poll.is_accepting_answers = serializer.validated_data["is_accepting_answers"]
        poll.save()

        return rf.Response(PollSerializer(poll).data, status=202)


class PollGetAnswer(APIView):
    queryset = Poll.objects.all()

    def get(self, request, poll_id=None, format=None):
        poll: Poll = get_object_or_404(Poll, pk=poll_id)

        if poll.is_accepting_answers:
            return HttpResponseBadRequest("Poll is still accepting answers")

        answer = Answer.objects.filter(question=poll.question, is_correct=True).first()

        return rf.Response(AnswerSerializer(answer).data, status=200)


class PollSubmitResponse(APIView):
    queryset = Poll.objects.all()
    serializer_class = PollSubmitResponseSerializer

    def put(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.is_poll_valid()

        poll: Poll = serializer.create(serializer.validated_data)
        answer: Answer = serializer.validated_data.pop("answer")
        response = Response.objects.create(poll=poll, answer=answer)

        return rf.Response(ResponseSerializer(response).data, status=201)
