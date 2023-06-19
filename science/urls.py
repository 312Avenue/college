from rest_framework.routers import DefaultRouter

from .views import NewsViews, ChapterViews


router = DefaultRouter()
router.register('news', NewsViews)
router.register('chapter', ChapterViews)

urlpatterns = []
urlpatterns += router.urls