from rest_framework.routers import DefaultRouter

from .views import TrainingViewSet

router = DefaultRouter()
router.register('schedule', TrainingViewSet)
urlpatterns = router.urls
