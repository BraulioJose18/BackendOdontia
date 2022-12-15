from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.user.api.serializer import *
from apps.user.models import *


class UserViewSet(ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_provider', 'is_worker', 'is_client']


class RoleViewSet(ModelViewSet):
    model = Role
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class PermissionViewSet(ModelViewSet):
    model = Permission
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
