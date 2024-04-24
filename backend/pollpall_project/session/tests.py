from django.urls import reverse
from django.test import Client, TestCase

from session.models import Session, Question
from session.views import Session

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

class TestQuestionModel(TestCase):
    
    @classmethod
    def setUpTest(cls): # To set up for each test in the class
        session = Session.objects.create(session_id=123, session_label='Test Session')
        
        Question.objects.create(questionID=1, question_text='Test question', session=session)
        
    def test_question_str_method(self):
        question = Question.objects.get(questionID=1)
        expected_result = "1: Test question: 1: Test Session"
        self.assertEqual(str(question), expected_result)

    def test_question_has_session(self):
        question = Question.objects.get(questionID=1)
        self.assertEqual(question.session.session_label, 'Test Session')

    def test_delete_session_cascades(self):
        session = Session.objects.get(session_label='Test Session')
        session.delete()
        self.assertFalse(Question.objects.filter(questionID=1).exists())

    