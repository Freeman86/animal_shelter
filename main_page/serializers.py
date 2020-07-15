from rest_framework import serializers

from .models import Main

class MainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        exclude = ("id",)