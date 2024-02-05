from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Session
import json

@method_decorator(csrf_exempt, name='dispatch')
class SessionView(View):
    def get(self, request, session_id=None):
        
        if session_id:
            session = get_object_or_404(Session, pk=session_id)
            data = {'session_id': session.session_id, 'session_label': session.session_label}
        else:
            sessions = Session.objects.all()
            data = [{'session_id': s.session_id, 'session_label': s.session_label} for s in sessions]

        return JsonResponse(data, safe=False)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        session_id = data['session_id']
        session_label = data['session_label']
        session = Session.objects.create(session_id=session_id, session_label=session_label)
        return JsonResponse({'session_id': session.session_id, 'session_label': session.session_label}, status=201)

    def delete(self, request, session_id):
        session = get_object_or_404(Session, pk=session_id)
        session.delete()
        return JsonResponse({'message': 'Session deleted successfully'})