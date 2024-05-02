import json
from django.urls import reverse
from django.test import Client, TestCase

from .models import *
from .views import *
from .serializers import *


class TestSessionService(TestCase):
    def setUp(self):
        self.client = Client()
        self.sessionStartURL = reverse("pollpal:session-start")

    def test_startSession_create_validPoll(self):

        # Arrange
        session = Session.objects.create(label="Session 1")
        question = Question.objects.create(prompt="Question 1")
        answer = Answer.objects.create(
            answer="Answer 1", question=question, is_correct=True
        )

        session.save()
        question.save()
        answer.save()

        data = {"session": session.id, "question": question.id}

        # Act
        response = self.client.post(
            self.sessionStartURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 201)
        poll: Poll = Poll.objects.get(pk=response.data["id"])

        self.assertEqual(poll.session.id, session.id)
        self.assertEqual(poll.question.id, question.id)
        self.assertTrue(poll.is_accepting_answers)
