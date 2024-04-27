from django.http import JsonResponse
from rest_framework import generics
from .models import Session, Question, Response, Poll
from .serializers import SessionSerializer


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = "session_id"


class SessionDestroy(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = "session_id"

class SessionService():
    
    def startSession(self, sessionid, question):
        try:
            session = Session.objects.get(session_id = sessionid)
        except:
                return JsonResponse({'error': 'Session does not exist'}, status=400)
    
        if Poll.objects.filter(session=session).exists():
            return JsonResponse({'error': 'Session already has a poll'}, status=400)
              
        new_poll = Poll.objects.create(
            session = session,
            question_id = Question.objects.get(question).question_id,
            related_question = question,
            is_accepting_answers = True
        )
        return JsonResponse({'message': 'Poll created successfully', 'poll_id': new_poll.poll_id}, status=201)



    def endSession(self, sessionid):
        try:
            session = Session.objects.get(session_id = sessionid)
        except:
            return JsonResponse({'error': 'Session does not exist'}, status=400)
        
        try:
            poll = Poll.objects.get(session = session)
        except:
            return JsonResponse({'error': 'No poll in session.'}, status = 400)

        poll.delete()
        
        return JsonResponse({'message': 'Poll deleted successfully'}, status=200)

