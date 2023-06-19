from rest_framework.routers import DefaultRouter

from .views import EmployeViewSet, PulpitViewSet


router = DefaultRouter()
router.register('employe', EmployeViewSet)
router.register('puplit', PulpitViewSet)

urlpatterns = []
urlpatterns += router.urls