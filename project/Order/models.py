from django.db import models


# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100)
    total_price = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    total_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
