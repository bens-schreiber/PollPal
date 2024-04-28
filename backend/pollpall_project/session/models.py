from django.db import models


class Session(models.Model):
    """
    Session Model

    Attributes
    label (str): Session Name
    """

    label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label}"


class Poll(models.Model):
    """
    Poll Model

    Attributes
    session (Session): Session which the poll is connected to
    question (Question): Question for the poll
    is_accepting_answers (bool): Whether the poll is accepting answers or not
    """

    session = models.OneToOneField("Session", on_delete=models.CASCADE)
    question = models.OneToOneField("Question", on_delete=models.CASCADE)
    is_accepting_answers = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.is_accepting_answers}"


class Question(models.Model):
    """
    Question Model

    Attributes:
    prompt (str): The question/prompt
    """

    prompt = models.CharField(max_length=0xFFF, default="")

    def __str__(self):
        return f"{self.prompt}"


class Answer(models.Model):
    """
    Answer Model

    Attributes
    answer (str): Text of the answer
    question (Question): The question this answer is connected to
    is_correct (bool): Whether this answer is correct or not
    """

    answer = models.CharField(max_length=0xFFF, default="")
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.answer}: {self.is_correct}"


class Response(models.Model):
    """
    Response Model

    Attributes
    answer (Answer): The answer which was chosen
    poll (Poll): The poll this response is connected to
    is_correct (bool): Whether the response was correct or not
    """

    answer = models.OneToOneField("Answer", on_delete=models.CASCADE)
    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.answer}: {self.is_correct}"
