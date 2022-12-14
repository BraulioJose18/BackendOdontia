from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.kardex.models import *
from apps.user.api.serializer import UserSerializer


class VoucherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherType
        fields = '__all__'


class KardexDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KardexDetail
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        movementType = instance.kardexHeader.movementType
        product = instance.product
        quantity = instance.quantity
        if movementType == 1:  # Compra
            product.stock += quantity
        elif movementType == 2:  # Venta
            if product.stock < quantity:
                raise ValidationError(detail='No hay suficiente stock de este producto')
            else:
                product.stock -= quantity
        product.save()
        return instance


class KardexHeaderSerializer(serializers.ModelSerializer):
    detail = KardexDetailSerializer(many=True)

    class Meta:
        model = KardexHeader
        fields = '__all__'

    def to_representation(self, obj):
        if 'branches' not in self.fields:
            self.fields['user'] = UserSerializer(obj, many=False)
            self.fields['voucherType'] = VoucherTypeSerializer(obj, many=False)
        return super(KardexHeaderSerializer, self).to_representation(obj)

    def create(self, validated_data):
        kardex_data = validated_data.pop('detail')
        instance = super().create(validated_data)
        for track_data in kardex_data:
            track_data['kardexHeader'] = instance.id
            track_data['product'] = track_data['product'].id
            kardexDetailSerializer = KardexDetailSerializer(data=track_data)
            kardexDetailSerializer.is_valid(raise_exception=True)
            kardexDetailSerializer.save()
        return instance
    # def create(self, validated_data):
    #     kardex_data = validated_data.pop('detail')
    #     header = KardexHeader.objects.create(**validated_data)
    #     for track_data in kardex_data:
    #         KardexDetail.objects.create(kardexHeader=header, **track_data)
    #     return header
