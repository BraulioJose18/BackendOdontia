from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.products.models import *


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

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['product'] = ProductSerializer(obj, many=False)
        return super(ExpirationSerializer, self).to_representation(obj)


# This serializer will allow us to customize our list field
class CustomExpirationSerializer(serializers.Serializer):
    dateExpiration = serializers.DateField()
    quantity = serializers.IntegerField()


# This is the serializer we will use in our custom CreateView, here have the personalized fields to use
class ExpirationCustomSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    details = serializers.ListField(child=CustomExpirationSerializer())


class ExampleExpirationGroupByProductSerializer(serializers.Serializer):
    id_product = serializers.IntegerField()
    name_product = serializers.CharField(max_length=256)
    stock_product = serializers.IntegerField()
    stock_expiration = serializers.IntegerField()


class AllExpirationList(serializers.Serializer):
    product = serializers.ListField(child=ProductSerializer())
    expiration = serializers.ListField(child=ExpirationSerializer())


class CustomPackStockProductSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    product = serializers.IntegerField()


class CreatePacksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=156)
    status = serializers.BooleanField()
    subcategory = serializers.IntegerField()
    measurementUnit = serializers.IntegerField()
    brand = serializers.IntegerField()
    salePrice = serializers.FloatField()
    purchasePrice = serializers.FloatField()
    specifications = serializers.CharField(max_length=156)
    observation = serializers.CharField(max_length=156)
    stock = serializers.IntegerField(default=0)
    # Stock Minimo
    minimumStock = serializers.IntegerField(default=0)
    # Stock Medio
    averageStock = serializers.IntegerField(default=0)
    hasExpiration = serializers.BooleanField(default=False)
    detailsProduct = serializers.ListField(child=CustomPackStockProductSerializer())


class PackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackDetail
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        totalQuantity = instance.packHeader.stock
        product = instance.product
        quantity = instance.quantity * totalQuantity
        product.stock -= quantity
        product.save()
        return instance


class PackHeaderSerializer(serializers.ModelSerializer):
    detail = PackDetailSerializer(many=True)

    class Meta:
        model = PackHeader
        fields = '__all__'

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['subcategory'] = SubCategorySerializer(obj, many=False)
            self.fields['measurementUnit'] = MeasurementUnitSerializer(obj, many=False)
            self.fields['brand'] = BrandSerializer(obj, many=False)
        return super(PackHeaderSerializer, self).to_representation(obj)

    def create(self, validated_data):
        pack_data = validated_data.pop('detail')
        instance = super().create(validated_data)
        for track_data in pack_data:
            track_data['packHeader'] = instance.id
            track_data['product'] = track_data['product'].id
            packDetailSerializer = PackDetailSerializer(data=track_data)
            packDetailSerializer.is_valid(raise_exception=True)
            packDetailSerializer.save()
        return instance




