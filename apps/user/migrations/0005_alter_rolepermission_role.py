# Generated by Django 4.1.2 on 2022-11-08 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_permission_rolepermission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolepermission',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='role', to='user.role'),
        ),
    ]
