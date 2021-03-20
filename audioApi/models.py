from django.db import models
from datetime import datetime

class participants(models.Model):
    name = models.CharField(max_length=100)

    def check_part(self):
        self.p = participants.objects.all()
        return len(self.p) > 10

class songFile(models.Model):
    songID = models.IntegerField()
    songName = models.CharField(max_length=100)
    songDuration = models.CharField(max_length=50)
    songUploaded = models.DateTimeField()


class podcastFile(models.Model):
    podID = models.IntegerField()
    podName = models.CharField(max_length=100)
    podDuration = models.CharField(max_length=50)
    podUploaded = models.DateTimeField()
    podHost = models.CharField(max_length=100)
    podParticipants = models.ForeignKey(participants, on_delete = models.CASCADE)


class AudioBookFile(models.Model):
    audioBookID = models.IntegerField()
    audioBookTitle = models.CharField(max_length=100)
    audioBookAuthor = models.CharField(max_length=100)
    audioBookNarrator = models.CharField(max_length=100)
    audioBookDuration = models.CharField(max_length=50)
    audioBookUploaded = models.DateTimeField()




    

