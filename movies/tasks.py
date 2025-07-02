from celery import shared_task
from PIL import Image
from .models import Movie
from django.conf import settings
from celery.exceptions import Retry

import os

@shared_task(bind=True, max_retries=5)
def generate_thumbnail(self, movie_id):
    movie = Movie.objects.get(id=movie_id)
    video_path = os.path.join(settings.MEDIA_ROOT, str(movie.video_file))

    if not os.path.exists(video_path):
        print(f"⏳ File not found: {video_path}. Retrying...")
        raise self.retry(countdown=3)

    thumbnail_path = os.path.splitext(video_path)[0] + "_thumb.jpg"
    img = Image.new("RGB", (1280, 720), color=(255, 0, 0))
    img.save(thumbnail_path)
    print(f"Thumbnail saved to: {thumbnail_path}")

@shared_task
def test_redis_connection():
    print("Redis and Celery are connected!")
    return "OK"
