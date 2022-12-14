from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from apps.products.models import *
from datetime import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['category'] = CategorySerializer(obj, many=False)
        return super(SubCategorySerializer, self).to_representation(obj)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['subcategory'] = SubCategorySerializer(obj, many=False)
            self.fields['measurementUnit'] = MeasurementUnitSerializer(obj, many=False)
            self.fields['brand'] = BrandSerializer(obj, many=False)
        return super(ProductSerializer, self).to_representation(obj)


class ExpirationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expiration
        fields = '__all__'

    def create(self, validated_data):
        detailExpiration = validated_data.pop('')

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['product'] = ProductSerializer(obj, many=False)
        return super(ExpirationSerializer, self).to_representation(obj)


class ExperitarionCustomnSerializer(serializers.Serializer):

    product = serializers.IntegerField()
    detailExpiration = ExpirationSerializer(many=True)

