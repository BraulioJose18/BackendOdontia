from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.api.views import *

router = DefaultRouter()
router.register(r'api/user', UserViewSet, basename='User')
router.register(r'api/role', RoleViewSet, basename='Role')
router.register(r'api/permission', PermissionViewSet, basename='Permission')
urlpatterns = router.urls
# urlpatterns += [
#     path("api-auth/", include("rest_framework.urls")),
# ]
# Swagger settings


