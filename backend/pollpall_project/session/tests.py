from rest_framework.test import APIRequestFactory
from django.test import TestCase

from .models import Session
from .views import SessionDetail

class TestSessionDetail(TestCase):
    def test_create_session(self):
        factory = APIRequestFactory()

        Session.objects.create(session_id = '123', session_label = 'first session')

        url = '/sessions/{}/'.format(Session.session_id)
        request = factory.get(url)
        view = SessionDetail.as_view()
        response = view(request, pk=Session.session_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['session_id'], Session.session_id)
        self.assertEqual(response.data['session_label'], Session.session_label)

    def test_delete_session(self):
        factory = APIRequestFactory()

        Session.objects.create(session_id = '123', session_label = 'test session')
        url = '/sessions/{}/'.format(Session.session_id)
        request = factory.delete(url)

        view = SessionDetail.as_view()
        response = view(request, pk = Session.session_id)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Session.objects.filter(pk=Session.pk).exists())