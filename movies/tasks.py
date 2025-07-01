import os
from celery import shared_task
from PIL import Image
from .models import Movie
from movie_project.settings import MEDIA_ROOT

@shared_task
def generate_thumbnail(movie_id):
    movie = Movie.objects.get(id=movie_id)
    video_path = os.path.join(MEDIA_ROOT, str(movie.video_file))
    thumbnail_path = os.path.splitext(video_path)[0] + "_thumb.jpg"

    img = Image.new("RGB", (1280, 720), color=(255, 0, 0))
    img.save(thumbnail_path)
