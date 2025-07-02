from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from .tasks import generate_thumbnail
from django.conf import settings
import os

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        movie = serializer.save()
        video_path = os.path.join(settings.MEDIA_ROOT, str(movie.video_file))
        if os.path.exists(video_path):
            generate_thumbnail.delay(movie.id)
        else:
            print(f"Video file not found yet: {video_path}")
