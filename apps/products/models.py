# Modelo de base de datos
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=156)
    status = models.BooleanField()

    class Meta:
        db_table = 'category'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Category'  # Como se muestra papi
        verbose_name_plural = 'Categories'  # ? :v

    # To String
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=156)
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategory'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Subcategory'  # Como se muestra papi
        verbose_name_plural = 'Subcategories'  # ? :v

    # To String
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=156)
    status = models.BooleanField()

    class Meta:
        db_table = 'brand'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Brand'  # Como se muestra papi
        verbose_name_plural = 'Brands'  # ? :v

    # To String
    def __str__(self):
        return self.name


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=156)
    symbol = models.CharField(max_length=156)
    status = models.BooleanField()

    class Meta:
        db_table = 'measurementUnit'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Measurement Unit'  # Como se muestra papi
        verbose_name_plural = 'Measurement Units'  # ? :v

    # To String
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=156)
    status = models.BooleanField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    measurementUnit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    salePrice = models.FloatField()
    purchasePrice = models.FloatField()
    specifications = models.CharField(max_length=156)
    observation = models.CharField(max_length=156)
    stock = models.IntegerField(default=0)
    #Stock Minimo
    minimumStock = models.IntegerField(default=0)
    #Stock Medio
    averageStock = models.IntegerField(default=0)
    hasExpiration = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Product'  # Como se muestra papi
        verbose_name_plural = 'Products'  # ? :v

    # To String
    def __str__(self):
        return self.name


class PackHeader(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=156)
    status = models.BooleanField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    measurementUnit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    salePrice = models.FloatField()
    specifications = models.CharField(max_length=156)
    observation = models.CharField(max_length=156)
    stock = models.IntegerField(default=0)

    class Meta:
        db_table = 'pack'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'Pack'  # Como se muestra papi
        verbose_name_plural = 'Packs'  # ? :v

    # To String
    def __str__(self):
        return self.name


class PackDetail(models.Model):
    packHeader = models.ForeignKey(PackHeader, on_delete=models.CASCADE, related_name='detail', blank=False, null=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'packdetail'
        abstract = False  # Clase abstracta :'v
        verbose_name = 'PackDetail'  # Como se muestra papi
        verbose_name_plural = 'PackDetails'  # ? :v


class Expiration(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    dateExpiration = models.DateField(blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'expiration'
        abstract = False
        verbose_name = 'Expiration'
        verbose_name_plural = 'Expirations'

    def __str__(self):
        return self.product.name
