from django.urls import reverse
from rest_framework.test import APIRequestFactory
from django.test import Client, TestCase

from .models import Session
from .views import Session

SESSION_POST = reverse('pollpal:session-list-create')

class TestSessionDetail(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_session(self):

        # Arrange
        sessionId = 123

        # Act
        response = self.client.post(SESSION_POST, {'session_id': sessionId, 'session_label': 'first session'}, format = 'json')

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Session.objects.filter(session_id=sessionId).exists())

    def test_delete_session(self):

        # Arrange 
        sessionId = 123
        self.client.post(SESSION_POST, {'session_id': sessionId, 'session_label': 'first session'}, format = 'json')

        # Act
        response = self.client.delete(reverse('pollpal:session-delete', kwargs = {'session_id': sessionId}))

        # Assert
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Session.objects.filter(session_id=sessionId).exists())