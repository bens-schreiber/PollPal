import json
from django.urls import reverse
from django.test import Client, TestCase

from .models import *
from .views import *
from .serializers import *


class TestSessionService(TestCase):
    def setUp(self):
        self.client = Client()
        self.sessionManagerURL = reverse("pollpal:session-manage")

    def test_startSession_create_validPoll(self):

        # Arrange
        session = Session.objects.create(label="Session")
        session.save()

        question = Question.objects.create(prompt="Test Starting Session")
        answer = Answer.objects.create(
            answer="Test answer", question=question, is_correct=True
        )
        data = {
            "session": SessionSerializer(session).data,
            "question": QuestionSerializer(question).data,
        }

        # Act
        response = self.client.post(
            self.sessionManagerURL, json.dumps(data), content_type="application/json"
        )
        # Assert
        self.assertEqual(response.status_code, 201)
        poll = Poll.objects.get(pk=response.data["id"])
        self.assertEqual(poll.session.id, session.id)
        self.assertTrue(poll.is_accepting_answers)
        self.assertIsNotNone(poll.question)

    def test_endSession_deleteNullPoll__returnsError(self):
        # Arrange
        session = Session.objects.create(label="Session")
        session.save()

        data = {"session": SessionSerializer(session).data}

        # Act
        response = self.client.delete(
            self.sessionManagerURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 400)

    def test_endSession_deletePoll_pollDeleted(self):
        # Arrange
        session = Session.objects.create(label="Session")
        session.save()

        poll = Poll.objects.create(prompt="Test Poll", session=session)
        poll.save()

        data = {
            "session": SessionSerializer(session).data,
            "poll": PollSerializer(poll).data,
        }

        # Act
        response = self.client.delete(
            self.sessionManagerURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 202)
        self.assertIsNone(len(list(Poll.objects.all)))
        self.assertIsNone(len(list(Question.objects.all)))
        self.assertIsNone(len(list(Response.objects.all)))
        self.assertIsNone(len(list(Answer.objects.all)))
