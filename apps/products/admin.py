#visualizar en el django admin la vista
from django.contrib import admin
from apps.products.models import *
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(MeasurementUnit)