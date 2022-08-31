from django.db import models
from django_countries.fields import CountryField


class Product(models.Model):
    product_Name = models.CharField(max_length=200)
    price = models.FloatField(default=0.00, blank=True)
    product_discriptions = models.TextField(max_length=100)
    country = CountryField()
    
    def __str__(self) -> str:
        return self.product_Name
