from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    release_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


####
def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "ProductImages/%s/%s.%s" % (
        instance.product.id,
        instance.product.id,
        extension,
    )


####


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Product_Images"
    )

    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.product.title


class Category(MPTTModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def _str_(self):
        return self.name
