import json
from django.test import TestCase
from django.urls import reverse
from .models import Session

class SessionViewTest(TestCase):
    def setUp(self):
        self.session = Session.objects.create(session_id='123', session_label='Test session')
        
    # Test GET method (status 200)
    def test_get_session(self):
        response = self.client.get(reverse('session-detail', args=['123']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'session_id' : 123, 'session_label' : 'Test session'})
        
    # Test POST method (status 201)
    def test_create_session(self):
        data = {'session_id': 1, 'session_label': 'Test Session'}
        response = self.client.post(reverse('session-list'), json.dumps(data), content_type='application/json')
        # Test JSon 201 code response (deleted)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Session.objects.filter(session_id=data['session_id'], session_label=data['session_label']).exists())
        
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data['session_id'], data['session_id'])
        self.assertEqual(response_data['session_label'], data['session_label'])

  # Test DELETE method (status 200)
    def test_delete_session(self):
        response = self.client.delete(reverse('session-detail', args=[self.session.session_id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Session.objects.filter(pk=self.session.session_id).exists())
        
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'message': 'Session deleted successfully'})