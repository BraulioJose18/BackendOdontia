# Modelo de base de datos
from django.db import models

from apps.products.models import Product
from apps.user.models import User


class VoucherType(models.Model):
    name = models.CharField(max_length=156)
    serie = models.CharField(max_length=4)
    status = models.BooleanField()

    class Meta:
        db_table = 'vouchertype'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'VoucherType'  # Como se muestra papi
        verbose_name_plural = 'Voucher Types'  # ? :v

    # To String
    def __str__(self):
        return self.name


class KardexHeader(models.Model):
    # Solo por si lo necesito ajuaaaaaaaaa :v
    id = models.AutoField(primary_key=True)
    movementType = models.IntegerField(default=1)  # 1->Compra 2->Venta
    date = models.DateField()
    totalPrice = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucherType = models.ForeignKey(VoucherType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'kardexheader'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'KardexHeader'  # Como se muestra papi
        verbose_name_plural = 'Kardex Headers'  # ? :v

    # To String
    def __str__(self):
        if self.movementType == 1:
            return 'K-' + self.voucherType.serie + '-' + str(self.id)
        else:
            return 'K-' + self.voucherType.serie + '-' + str(self.id)


class KardexDetail(models.Model):
    kardexHeader = models.ForeignKey(KardexHeader, on_delete=models.PROTECT, related_name='detail', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    totalPrice = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'kardexdetail'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'KardexDetail'  # Como se muestra papi
        verbose_name_plural = 'Kardex Details'  # ? :v

    # To String
    def __str__(self):
        if self.movementType == 1:
            return 'K-D' + self.voucherType.serie + '-' + str(self.id)
        else:
            return 'K-D' + self.voucherType.serie + '-' + str(self.id)
