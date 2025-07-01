from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer
from .tasks import generate_thumbnail

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        movie = serializer.save()
        generate_thumbnail.delay(movie.id)
