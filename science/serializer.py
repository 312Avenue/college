from rest_framework import serializers

from .models import Chapter, News


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'
        