from rest_framework.routers import DefaultRouter
from apps.kardex.api.views import *

router = DefaultRouter()
router.register(r'api/vouchertype', VoucherTypeViewSet, basename='VoucherType')
router.register(r'api/purchase_sale', KardexHeaderViewSet, basename='KardexHeader')
router.register(r'api/kardexdetail', KardexDetailViewSet, basename='KardexDetail')
urlpatterns = router.urls

