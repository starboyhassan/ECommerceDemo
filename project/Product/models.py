from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    release_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey("category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.title


class category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
