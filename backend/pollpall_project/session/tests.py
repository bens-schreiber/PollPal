from django.urls import reverse
from django.test import Client, TestCase

from .models import Poll, Session, Question
from .views import Session, SessionService

SESSION_POST = reverse("pollpal:session-list-create")


class TestSessionDetail(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_session(self):

        # Arrange
        sessionId = 123

        # Act
        response = self.client.post(
            SESSION_POST,
            {"session_id": sessionId, "session_label": "first session"},
            format="json",
        )

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Session.objects.filter(session_id=sessionId).exists())

    def test_delete_session(self):

        # Arrange
        sessionId = 123
        self.client.post(
            SESSION_POST,
            {"session_id": sessionId, "session_label": "first session"},
            format="json",
        )

        # Act
        response = self.client.delete(
            reverse("pollpal:session-delete", kwargs={"session_id": sessionId})
        )

        # Assert
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Session.objects.filter(session_id=sessionId).exists())

class TestSessionService(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_start_session(self):
        
        #Arrange
        sessionID = 123
        questionID = 789
        self.client.post(SESSION_POST, {'session_id': sessionID, 'session_label': 'first session'}, format = 'json')
        
        question = Question.objects.create(
            question_id = questionID,
            prompt = 'Test prompt',
        )
        
        #Act    
        response = SessionService.startSession(self, sessionID, question)
        self.assertEqual(response.status_code, 201)
        
