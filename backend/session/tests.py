import json
from django.urls import reverse
from rest_framework.test import APIRequestFactory
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
        session = Session.objects.create(pk=1, label="Session")
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
        self.assertIsNotNone(question.poll)

    # def test_create_session(self):

    #     # Arrange
    #     sessionId = 123

    #     # Act
    #     response = self.client.post(
    #         SESSION_POST,
    #         {"session_id": sessionId, "session_label": "first session"},
    #         format="json",
    #     )

    #     # Assert
    #     self.assertEqual(response.status_code, 201)
    #     self.assertTrue(Session.objects.filter(session_id=sessionId).exists())

    # def test_delete_session(self):

    #     # Arrange
    #     sessionId = 123
    #     self.client.post(
    #         SESSION_POST,
    #         {"session_id": sessionId, "session_label": "first session"},
    #         format="json",
    #     )

    #     # Act
    #     response = self.client.delete(
    #         reverse("pollpal:session-delete", kwargs={"session_id": sessionId})
    #     )

    #     # Assert
    #     self.assertEqual(response.status_code, 204)
    #     self.assertFalse(Session.objects.filter(session_id=sessionId).exists())
