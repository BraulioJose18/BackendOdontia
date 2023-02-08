# Generated by Django 4.1.2 on 2023-02-08 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_hasexpiration_remove_expiration_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=156)),
                ('status', models.BooleanField()),
                ('salePrice', models.FloatField()),
                ('specifications', models.CharField(max_length=156)),
                ('observation', models.CharField(max_length=156)),
                ('stock', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('measurementUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measurementunit')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
            options={
                'verbose_name': 'Pack',
                'verbose_name_plural': 'Packs',
                'db_table': 'pack',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('packHeader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='products.packheader')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'PackDetail',
                'verbose_name_plural': 'PackDetails',
                'db_table': 'packdetail',
                'abstract': False,
            },
        ),
    ]
