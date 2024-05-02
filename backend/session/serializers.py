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


# APIView serializers


class SessionStartSerializer(serializers.Serializer):
    session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    def create(self, validated_data):
        """Creates a Poll object from the validated data and saves it in the database"""
        question: Question = validated_data.pop("question")

        poll: Poll = Poll.objects.create(is_accepting_answers=True, **validated_data)

        question.poll = poll
        question.save()
        return poll
