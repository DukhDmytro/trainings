from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Training
from .serializers import TrainingsSerializer


class TrainingViewSet(ModelViewSet):
    """Viewset for trainings"""
    queryset = Training.objects.all()
    serializer_class = TrainingsSerializer
    lookup_field = 'id'
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = IsAdminUser,
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = IsAdminUser,
        else:
            self.permission_classes = IsAuthenticated,
        return super().get_permissions()
