from django.contrib import admin
from . models import participants, podcastFile, songFile, AudioBookFile

admin.site.register(participants)
admin.site.register(podcastFile)
admin.site.register(songFile)
admin.site.register(AudioBookFile)
