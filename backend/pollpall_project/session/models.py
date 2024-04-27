from django.db import models

class Session(models.Model):
    session_id = models.IntegerField(primary_key=True)
    session_label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.session_id}: {self.session_label}"


class Poll(models.Model):
    """
    Holds the current poll

    Attributes:
        poll_id (int): Primary key of model
        session (Session): Session which this poll is connected to
        question_id (int): Integer ID of current question
        related_question (Question): Current question
        is_accepting_answers (bool): Whether the poll is accepting and updating answers.
    """

    poll_id = models.IntegerField(primary_key=True)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    question_id = models.IntegerField(default=-1)
    related_question = models.ForeignKey(
        "Question", on_delete=models.CASCADE, related_name="related_polls"
    )
    is_accepting_answers = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.poll_id}: {self.session}: {self.question_id}: {self.related_question}: {self.is_accepting_answers}"


class Question(models.Model):
    """
    Holds the question we are asking

    Attributes:
        question_id (int): The primary key of the model
        prompt (str): The question we are asking
        poll (Poll): The poll this question comes from
    """

    question_id = models.IntegerField(primary_key=True)
    prompt = models.CharField(max_length=0xFFF, default="")
    poll = models.ForeignKey(
        "Poll", on_delete=models.CASCADE, related_name="related_questions"
    )

    def __str__(self):
        return f"{self.question_id}: {self.prompt}: {self.related_poll}"


class Response(models.Model):
    """
    Holds a response to the linked question

    Attributes:
        response_id (int): Primary key of the model
        prompt (str): The response
        question (Question): The question this response comes from
        is_correct (bool): Whether the question is true or not
    """

    response_id = models.IntegerField(primary_key=True)
    prompt = models.CharField(max_length=0xFFF, default="")
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.response_id}: {self.prompt}: {self.question}: {self.is_correct}"
