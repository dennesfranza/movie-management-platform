import os
import subprocess
from django.conf import settings
from movies.models import Movie  # adjust import as needed
from celery.exceptions import Retry
from celery import shared_task

@shared_task(bind=True, max_retries=3)
def generate_thumbnail(self, movie_id):
    movie = Movie.objects.get(id=movie_id)
    video_path = os.path.join(settings.MEDIA_ROOT, str(movie.video_file))

    if not os.path.exists(video_path):
        print(f"⏳ File not found: {video_path}. Retrying...")
        raise self.retry(countdown=3)

    # Define output thumbnail path
    thumbnail_path = os.path.splitext(video_path)[0] + "_thumb.jpg"

    # Use ffmpeg to extract a frame at 1 second (adjust as needed)
    try:
        subprocess.run([
            'ffmpeg',
            '-ss', '00:00:01',        # Seek to 1 second
            '-i', video_path,         # Input video
            '-frames:v', '1',         # Only one frame
            '-q:v', '2',              # Quality level (1 is best, 31 is worst)
            thumbnail_path
        ], check=True)
        print(f"Thumbnail saved to: {thumbnail_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate thumbnail: {e}")
        raise self.retry(countdown=5)
