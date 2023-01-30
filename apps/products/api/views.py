from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.products.api.serializer import *
from apps.products.api.utils import CustomExpirationProduct
from apps.products.models import *

from django.db import connection


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
    queryset = Expiration.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'dateExpiration']


# Here we use the CrateAPIView to have the 'form' format by Swagger and DRF (only crate)
class ExpirationCustomViewSet(CreateAPIView):
    serializer_class = ExpirationCustomSerializer

    # Post method customized
    def post(self, request, *args, **kwargs):
        # Receive the data customized by Serializer
        serializer = ExpirationCustomSerializer(data=request.data)
        # We validated the format
        if serializer.is_valid():
            # Verify the product exist
            try:
                # Get product sent
                product = Product.objects.get(pk=serializer.data.pop('product'))
            except Product.DoesNotExist:
                return Response(
                    {
                        'message': 'Product does not exist',
                        'product': serializer.data.pop('product')
                    }, status=status.HTTP_400_BAD_REQUEST)

            # Obtain the list data in details
            criteria_data = serializer.data.pop('details')
            # Gets each element of the previous list
            for track_data in criteria_data:
                # Create the expiration object with product
                Expiration.objects.create(product=product, **track_data)

            return Response(
                {
                    'message': 'Expiration by products create correctly.',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)

        return Response(
            {
                'message': 'No valid data',
                'data': serializer.data
            }, status=status.HTTP_400_BAD_REQUEST)


class ExpirationUpdateCustomViewSet(UpdateAPIView):
    serializer_class = ExpirationCustomSerializer

    def patch(self, request, *args, **kwargs):
        serializer = ExpirationCustomSerializer(data=request.data)

        if serializer.is_valid():
            product = Product.objects.get(pk=serializer.data.pop('product'))
            expiration = Expiration.objects.filter(product=product)
            print(expiration)

        return Response(
            {
                'message': '200',
                'data': 'ASDA'
            }, status=status.HTTP_200_OK)


class AllExpirationListViewSet(ListAPIView):

    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.callproc('GET_ALL_PRODUCTS_WITH_DIFERENT_STOCK')
        all_product_stock_diferent = cursor.fetchall()
        obj_all_product_stock_diferent = [CustomExpirationProduct(*x) for x in all_product_stock_diferent]
        json = ExampleExpirationGroupByProductSerializer(obj_all_product_stock_diferent, many=True).data
        return Response(
            {
                'message': '200',
                'data': json
            }, status=status.HTTP_200_OK)
