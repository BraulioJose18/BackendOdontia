from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from apps.kardex.api.serializer import *
from apps.kardex.models import *
from apps.products.models import Product


class VoucherTypeViewSet(ModelViewSet):
    model = VoucherType
    serializer_class = VoucherTypeSerializer
    queryset = VoucherType.objects.all()


class KardexHeaderViewSet(ModelViewSet):
    model = KardexHeader
    serializer_class = KardexHeaderSerializer
    queryset = KardexHeader.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['movementType']

class KardexDetailViewSet(ModelViewSet):
    product = Product.objects.filter()
    model = KardexDetail
    serializer_class = KardexDetailSerializer
    queryset = KardexDetail.objects.all()



