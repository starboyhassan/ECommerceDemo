# Generated by Django 4.2.4 on 2023-08-06 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Product", "0005_remove_product_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="produc_images",
                to="Product.product",
            ),
        ),
    ]
