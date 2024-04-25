from rest_framework import generics
from .models import Session, Question, Response, Poll
from .serializers import SessionSerializer

class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'session_id'
    
class SessionDestroy(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'session_id'

# TODO
class PollService():
    
    # Clean these up
    
    @staticmethod
    def nextQuestion(poll_id, question):
        try:
            poll = Poll.objects.get(id=poll_id)
            poll.question = question
            poll.save()
            return True
        except Poll.DoesNotExist:
            return False
    
    @staticmethod
    def haltReceivingAnswers(poll_id):
        try:
            poll = Poll.objects.get(id=poll_id)
            poll.is_accepting_answers = False
            poll.save()
            return True
        except Poll.DoesNotExist:
            return False
    
    @staticmethod
    def getAnswer(poll_id):
        try:
            poll = Poll.objects.get(id=poll_id)
            if not poll.is_accepting_answers:
                # Get poll CORRECT answer
                return poll.answer
            else:
                return None
        except Poll.DoesNotExist:
            return None

    @staticmethod
    def submitResponse(poll_id, response):
        try:
            poll = Poll.objects.get(id=poll_id)
            poll_response = Response.objects.create(poll=poll, response=response)
            poll_response.save()
            return True
        except Poll.DoesNotExist:
            return False


# TODO
class SessionService():
    @staticmethod
    def startSession(session_id, initial_question):
        try:
            session = Session.objects.get(id=session_id)
            poll = Poll.objects.create(session=session, current_question=initial_question)
            poll.save()
            return True
        except Session.DoesNotExist:
            return False
    
    @staticmethod
    def endSession(session_id):
        try:
            poll = Poll.objects.get(session__id=session_id)
            poll.delete()
            return True
        except Poll.DoesNotExist:
            return False
