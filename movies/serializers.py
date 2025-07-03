from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(required=False)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_video_file(self, value):
        if not value:
            return value
        if value.size > 100 * 1024 * 1024:
            raise serializers.ValidationError("Max file size is 100MB")
        if not value.name.endswith(('.mp4', '.mov', '.avi')):
            raise serializers.ValidationError("Unsupported file format")
        return value
