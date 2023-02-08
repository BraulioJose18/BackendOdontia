from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.products.api.views import *

router = DefaultRouter()
router.register(r'api/category', CategoryViewSet, basename='Category')
router.register(r'api/subcategory', SubCategoryViewSet, basename='Subcategory')
router.register(r'api/brand', BrandViewSet, basename='Brand')
router.register(r'api/measurement_unit', MeasurementUnitViewSet, basename='MeasurementUnit')
router.register(r'api/product', ProductViewSet, basename='Product')
router.register(r'api/expiration', ExpirationViewSet, basename='Expiration')
router.register(r'api/pack', PackHeaderViewSet, basename='PackHeader')
router.register(r'api/packDetail', PackDetailsViewSet, basename='PackDetail')

urlpatterns = router.urls
# urlpatterns += [
#    path('api/product/expiration/custom/', ExpirationCustomViewSet.as_view())
# ]
