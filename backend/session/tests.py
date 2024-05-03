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

        data = {"session": session.id}

        # Act
        response = self.client.delete(
            self.sessionEndURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 202)
        self.assertTrue(Session.objects.filter(pk=session.id).exists())

        self.assertFalse(Poll.objects.exists())
        self.assertFalse(Response.objects.exists())
        self.assertFalse(Question.objects.exists())
        self.assertFalse(Answer.objects.exists())

    def test_endSession_deleteNullPoll_doNothing(self):
        # Arrange
        session = Session.objects.create(label="Session 1")

        data = {"session": session.id}

        # Act
        response = self.client.delete(
            self.sessionEndURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertTrue(Session.objects.exists())
        self.assertFalse(Poll.objects.exists())

    def test_endSession_deletePollAcceptingAnswers_doNothing(self):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=True)

        data = {"session": session.id}

        # Act
        response = self.client.delete(
            self.sessionEndURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertTrue(Session.objects.exists())
        self.assertTrue(Poll.objects.exists())


class TestPollService(TestCase):
    def setUp(self):
        self.client = Client()
        self.nextQuestionURL = reverse("pollpal:poll-next-question")
        self.setAcceptingAnswerURL = reverse("pollpal:poll-set-accepting-answer")
        self.getAnswerURL = reverse("pollpal:poll-get-correct-answer")

    def test_nextQuestion_setNewQuestion_setsNewQuestion(self):

        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=False)
        old_question = Question.objects.create(prompt="Old Question", poll=poll)
        new_question = Question.objects.create(prompt="New Question")
        old_response = Response.objects.create(poll=poll, is_correct=True)
        old_question_answer = Answer.objects.create(
            answer="Old Answer",
            question=old_question,
            is_correct=True,
            response=old_response,
        )
        new_question_answer = Answer.objects.create(
            answer="New Answer",
            question=new_question,
            is_correct=True,
        )

        data = {"poll": poll.id, "question": new_question.id}

        # Act

        response = self.client.post(
            self.nextQuestionURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        poll: Poll = Poll.objects.get(pk=response.data["id"])
        self.assertFalse(Question.objects.filter(pk=old_question.id).exists())
        self.assertFalse(Answer.objects.filter(pk=old_question_answer.id).exists())
        self.assertEqual(poll.question.id, new_question.id)

    def test_nextQuestion_isAcceptingAnswers_DoNothing(self):

        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=True)
        old_question = Question.objects.create(prompt="Old Question", poll=poll)
        new_question = Question.objects.create(prompt="New Question")

        data = {"poll": poll.id, "question": new_question.id}

        # Act

        response = self.client.post(
            self.nextQuestionURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertEqual(poll.question.id, old_question.id)

    def test_setAcceptingAnswers_isAcceptingAnswersAndHasQuestion_isNotAcceptingAnswers(
        self,
    ):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=True)
        question = Question.objects.create(poll=poll, prompt="Test Question")

        data = {"poll": poll.id}

        # Act
        response = self.client.patch(
            self.setAcceptingAnswerURL,
            json.dumps(data),
            content_type="application/json",
        )

        # Assert
        poll: Poll = Poll.objects.get(pk=response.data["id"])
        self.assertEqual(response.status_code, 202)
        self.assertFalse(poll.is_accepting_answers)

    def test_setAcceptingAnswers_isNotAcceptingAnswersAndHasQuestion_isAcceptingAnswers(
        self,
    ):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=False)
        question = Question.objects.create(poll=poll, prompt="Test Question")

        data = {"poll": poll.id}

        # Act
        response = self.client.patch(
            self.setAcceptingAnswerURL,
            json.dumps(data),
            content_type="application/json",
        )

        # Assert
        poll: Poll = Poll.objects.get(pk=response.data["id"])
        self.assertEqual(response.status_code, 202)
        self.assertTrue(poll.is_accepting_answers)

    def test_setAcceptingAnswers_hasNoQuestion_doNothing(self):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=False)

        data = {"poll": poll.id, "is_accepting_answers": True}

        # Act
        response = self.client.patch(
            self.setAcceptingAnswerURL,
            json.dumps(data),
            content_type="application/json",
        )

        # Assert
        self.assertEqual(response.status_code, 400)

    def test_getAnswer_isAcceptingAnswers_doNothing(self):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=True)
        question = Question.objects.create(poll=poll, prompt="Test Question")
        answer = Answer.objects.create(
            answer="Test Correct Answer", question=question, is_correct=True
        )

        data = {"poll": poll.id}

        # Act
        response = self.client.get(
            self.getAnswerURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 400)

    def test_getAnswer_isNotAcceptingAnswers_getCorrectAnswer(self):
        # Arrange
        session = Session.objects.create(label="Session 1")
        poll = Poll.objects.create(session=session, is_accepting_answers=True)
        question = Question.objects.create(poll=poll, prompt="Test Question")
        answer = Answer.objects.create(
            answer="Test Correct Answer", question=question, is_correct=True
        )

        data = {"poll": poll.id}

        # Act
        response = self.client.get(
            self.getAnswerURL, json.dumps(data), content_type="application/json"
        )

        # Assert
        self.assertEqual(response.status_code, 200)
        got_answer: Answer = Answer.objects.get(pk=response.data["id"])
        self.assertEqual(answer, got_answer)
