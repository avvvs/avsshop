# Generated by Django 4.2 on 2023-05-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_producttype_product_discount_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
