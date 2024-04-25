from django.db import models
from .models import Question

class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)
    session_label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.session_id}: {self.session_label}"

# TODO
# By using ForeignKey, each question should be automatically connected to the poll
# that fetches it (Not figured out). Each response is also connected to it's respective
# question, so we shouldn't need a list of responses.
class Poll(models.Model):
    poll_id = models.IntegerField(primary_key=True) 
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question_id = models.IntegerField(default=-1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_accepting_answers = models.BooleanField(default=False)

class Question(models.Model): # Just holds a question ID and the question
    question_id = models.IntegerField(primary_key=True) 
    prompt = models.CharField(max_length=0xFFF)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE) # If session is deleted, also delete question from database.
    
    def __str__(self):
        return f"{self.question_id}: {self.prompt}: {self.session}"

class Response(models.Model): # Holds a response and whether it is the correct answer or not.
    response_id = models.IntegerField(primary_key=True)
    prompt = models.CharField(max_length=0xFFF)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Connects Response to Question.
    is_correct = models.BooleanField(default=False)