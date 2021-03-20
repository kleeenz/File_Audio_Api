from rest_framework.response import Response
from rest_framework import viewsets
from .models import participants, songFile, podcastFile, AudioBookFile
from .serializers import participantSerializer, songFileSerializer, podcastFileSerializer, AudioBookSerializer


class participantViewset(viewsets.ModelViewSet):
    serializer_class = participantSerializer
    queryset = participants.objects.all()


class songFileViewset(viewsets.ModelViewSet):
    serializer_class = songFileSerializer
    queryset = songFile.objects.all()

class podcastFileViewset(viewsets.ModelViewSet):
    queryset = podcastFile.objects.all()
    serializer_class = podcastFileSerializer

class AudioBookFileviewset(viewsets.ModelViewSet):
    queryset = AudioBookFile.objects.all()
    serializer_class = AudioBookSerializer



