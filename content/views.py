from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Content, Img, File, Comment
from .serializer import ContentSerializer, ImgSerializer, FileSerializer, CommentSerializer
from .permissions import IsAuthor


class ContentViewsSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'list':
            return ContentSerializer
        return super().get_serializer_class()
        
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthor]
        elif self.action in ['destroy']:
            self.pagination_class = [IsAdminUser]
        return super().get_permissions()