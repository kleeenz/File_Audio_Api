from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'part', views.participantViewset, basename='part')
router.register(r'song', views.songFileViewset, basename='song')
router.register(r'podcast', views.podcastFileViewset, basename="podcast")
router.register(r'audio', views.AudioBookFileviewset, basename="audio")


urlpatterns = router.urls