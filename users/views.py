from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination

from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    User view set
    """
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        """
        Unauthorised user can only register.
        All other methods available for admin user only
        """
        if self.action == 'create':
            self.permission_classes = AllowAny,
        else:
            self.permission_classes = IsAuthenticated, IsAdminUser
        return super().get_permissions()
