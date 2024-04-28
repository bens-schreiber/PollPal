from django.db import models


class Session(models.Model):
    label = models.CharField(max_length=255)
    poll = models.OneToOneField("Poll", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.label}"


class Poll(models.Model):
    question = models.OneToOneField("Question", on_delete=models.CASCADE, null=True)
    responses = models.ForeignKey("Response", on_delete=models.CASCADE, null=True)
    is_accepting_answers = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question}: {self.is_accepting_answers}"


class Question(models.Model):
    prompt = models.CharField(max_length=0xFFF, default="")

    def __str__(self):
        return f"{self.prompt}"


class Response(models.Model):
    answer = models.OneToOneField(
        "Answer",
        on_delete=models.CASCADE,
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.answer}: {self.is_correct}"


class Answer(models.Model):
    answer = models.CharField(max_length=0xFFF, default="")
    is_correct = models.BooleanField(default=False)
