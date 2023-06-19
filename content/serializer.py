from rest_framework import serializers

from .models import Content, Img, File, Comment


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ('img', 'id')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'id')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = ['author', 'text', 'rating', 'create_date', 'id']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user

        return super().create(validated_data)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['img'] = ImgSerializer(instance.image.all(), many=True).data
        represent['file'] = FileSerializer(instance.file.all(), many=True).data
        represent['comments'] = CommentSerializer(instance.comment.all(), many=True).data
        rating = [dict(i)['rating'] for i in dict(represent)['comments'] if dict(i)['rating'] != None]
        if rating:
            represent['rating'] = round((sum(rating) / len(rating)), 2)
            return represent
        else:
            represent['rating'] = None
            return represent