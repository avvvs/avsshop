# Generated by Django 4.2 on 2023-05-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='page_description',
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
