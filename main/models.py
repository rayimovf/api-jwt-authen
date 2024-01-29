from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=70)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=3)
    information = models.TextField()

    def __str__(self):
        return self.name

