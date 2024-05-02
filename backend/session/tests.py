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
        self.sessionEndURL = reverse("pollpal:session-end")

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

    def test_endSession_delete_deletePollandCascadingFields(self):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=False)
        response = Response.objects.create(poll=poll, is_correct=True)
        question = Question.objects.create(prompt="Question 1", poll=poll)
        answer = Answer.objects.create(
            answer="Answer 1", question=question, is_correct=True, response=response
        )

        session.save()
        poll.save()
        response.save()
        question.save()
        answer.save()

        data = {"session": session.id}

        # Act
        response = self.client.delete(
            self.sessionEndURL, json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 202)
        self.assertTrue(Session.objects.filter(pk=poll.id).exists())

        self.assertFalse(Poll.objects.exists())
        self.assertFalse(Response.objects.exists())
        self.assertFalse(Question.objects.exists())
        self.assertFalse(Answer.objects.exists())

    def test_endSession_deleteNullPoll_doNothing(self):
        # Arrange
        session = Session.objects.create(label="Session 1")

        session.save()

        data = {"session": session.id}

        # Act
        response = self.client.delete(
            self.sessionEndURL, json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertTrue(Session.objects.exists())
        self.assertFalse(Poll.objects.exists())

    def test_endSession_deletePollAcceptingAnswers_doNothing(self):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=True)

        session.save()

        data = {"session": session.id}

        # Act
        response = self.client.delete(
            self.sessionEndURL, json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertTrue(Session.objects.exists())
        self.assertTrue(Poll.objects.exists())
