# Generated by Django 4.1.2 on 2022-11-08 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_role_permission'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RolePermission',
        ),
    ]
