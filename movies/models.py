from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
