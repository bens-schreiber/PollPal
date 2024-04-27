from rest_framework import serializers
from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ("session_id", "session_label")

    lookup_field = "session_id"
