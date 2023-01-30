"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions

from apps.products.api.views import ExpirationCustomViewSet, ExpirationUpdateCustomViewSet, AllExpirationListViewSet
from apps.user.api.urls import router as user_router
from apps.products.api.urls import router as product_router
from apps.kardex.api.urls import router as kardex_router
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Documentation API",
        default_version='v0.1',
        description="Documentation API-Accreditation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jfarfanc@unsa.edu.pe"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


class DefaultRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)


router = DefaultRouter()
router.extend(user_router)
router.extend(product_router)
router.extend(kardex_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('', include('apps.user.api.urls')),
    # path('', include('apps.products.api.urls')),
    # path('', include('apps.kardex.api.urls')),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Custom view create in app product
    path('api/product/expiration/custom/', ExpirationCustomViewSet.as_view()),
    path('api/product/expiration/customUpdate', ExpirationUpdateCustomViewSet.as_view()),
    path('api/product/expiration/all', AllExpirationListViewSet.as_view())
]

# Swagger and redoc documentation
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
