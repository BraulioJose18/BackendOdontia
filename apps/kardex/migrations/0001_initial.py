# Generated by Django 4.1.2 on 2022-10-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=156)),
                ('serie', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'VoucherType',
                'verbose_name_plural': 'Voucher Types',
                'db_table': 'vouchertype',
                'abstract': False,
            },
        ),
    ]
