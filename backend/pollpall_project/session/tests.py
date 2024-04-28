from django.urls import reverse
from django.test import Client, TestCase

from .models import Poll, Session, Question
from .views import Session

SESSION_POST = reverse("pollpal:session-list-create")


class TestSessionDetail(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_session(self):

        # Act
        response = self.client.post(
            SESSION_POST,
            {"session_label": "first session"},
            format="json",
        )

        # Assert
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Session.objects.filter(id=1).exists())

    def test_delete_session(self):

        # Arrange
        self.client.post(
            SESSION_POST, {"session_label": "first session"}, format="json"
        )

        # Act
        response = self.client.delete(reverse("pollpal:session-delete", kwargs={1}))

        # Assert
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Session.objects.filter(1).exists())
