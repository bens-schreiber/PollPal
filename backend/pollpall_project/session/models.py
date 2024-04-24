from django.db import models

class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)
    session_label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.session_id}: {self.session_label}"

class Question(models.Model): # Just holds a question ID and the question
    questionID = models.IntegerField(primary_key=True) 
    question_text = models.CharField(max_length=255)
    session = models.ForeignKey(Session, on_delete=models.CASCADE) # If session is deleted, also delete question from database.
    
    def __str__(self):
        return f"{self.questionID}: {self.question_text}: {self.session}"