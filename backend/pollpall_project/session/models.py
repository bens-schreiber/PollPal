from django.db import models
from .models import Question


class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)
    session_label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.session_id}: {self.session_label}"


# TODO
# By using ForeignKey, each question should be automatically connected to the poll
# that fetches it. Each response is also connected to it's respective
# question, so we shouldn't need a list of responses.
class Poll(models.Model):
    poll_id = models.IntegerField(primary_key=True)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    question_id = models.IntegerField(default=-1)
    related_question = models.ForeignKey(
        "Question", on_delete=models.CASCADE, related_name="related_polls"
    )
    is_accepting_answers = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.poll_id}: {self.session}: {self.question_id}: {self.related_question}: {self.is_accepting_answers}"


class Question(models.Model):  # Just holds a question ID and the question
    question_id = models.IntegerField(primary_key=True)
    prompt = models.CharField(max_length=0xFFF)
    related_poll = models.ForeignKey(
        "Poll", on_delete=models.CASCADE, related_name="related_questions"
    )  # If poll is deleted, also delete question from database.

    def __str__(self):
        return f"{self.question_id}: {self.prompt}: {self.related_poll}"


class Response(
    models.Model
):  # Holds a response and whether it is the correct answer or not.
    response_id = models.IntegerField(primary_key=True)
    prompt = models.CharField(max_length=0xFFF)
    # Foreign key should cover One-to-Many connection
    question = models.ForeignKey(
        "Question", on_delete=models.CASCADE
    )  # Connects Response to Question.
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.response_id}: {self.prompt}: {self.question}: {self.is_correct}"
