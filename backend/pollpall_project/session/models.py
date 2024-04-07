from django.db import models


class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)
    session_label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.session_id}: {self.session_label}"

class Poll(models.Model):
    poll_id = models.IntegerField(primary_key=True)
    poll = models.CharField(max_length=255)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class Answer(models.Model):
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    num_votes = models.IntegerField(default=0)