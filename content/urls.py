from rest_framework.routers import DefaultRouter

from .views import ContentViewsSet, CommentViewSet


router = DefaultRouter()
router.register('content', ContentViewsSet)
router.register('content/comment', CommentViewSet)

urlpatterns = []
urlpatterns += router.urls
