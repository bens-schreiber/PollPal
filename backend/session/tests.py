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
