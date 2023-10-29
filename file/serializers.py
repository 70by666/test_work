from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import File


class FileSerializer(ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = File
        fields = '__all__'
