# Generated by Django 5.1.7 on 2025-03-24 13:06

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR', unique=True)),
                ('national_id_number', models.IntegerField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_of_each_user', to='product.product')),
            ],
        ),
    ]
