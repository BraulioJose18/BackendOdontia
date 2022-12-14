from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from apps.products.api.serializer import *
from apps.products.models import *
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(ModelViewSet):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'status']


class SubCategoryViewSet(ModelViewSet):
    model = SubCategory
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class BrandViewSet(ModelViewSet):
    model = Brand
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class MeasurementUnitViewSet(ModelViewSet):
    model = MeasurementUnit
    serializer_class = MeasurementUnitSerializer
    queryset = MeasurementUnit.objects.all()


class ProductViewSet(ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ExpirationViewSet(ModelViewSet):
    model = Expiration
    serializer_class = ExpirationSerializer
    queryset = Expiration.objects.all()


class ExpirationCustomViewSet(APIView):

    def post(self, request):
        results = ExperitarionCustomnSerializer(data=request.data)
        return Response({'data': results.data}, status=status.HTTP_200_OK)
