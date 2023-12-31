# Generated by Django 4.2.4 on 2023-08-06 16:19

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="category_name",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to=Product.models.image_upload),
        ),
    ]
