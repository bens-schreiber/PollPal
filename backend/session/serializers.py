from rest_framework import serializers
from .models import Session, Poll, Question, Response, Answer


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = "__all__"


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
