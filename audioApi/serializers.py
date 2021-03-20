from rest_framework import serializers
from .models import participants, songFile, podcastFile, AudioBookFile


class participantSerializer(serializers.ModelSerializer):
    class Meta:
        model = participants
        fields = '__all__'

class songFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = songFile
        fields = '__all__'


class podcastFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = podcastFile
        fields = '__all__'


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBookFile
        fields = '__all__'