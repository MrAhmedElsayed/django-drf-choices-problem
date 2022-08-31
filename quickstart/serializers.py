from .models import Product
from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin


class ProductSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country = CountryField(country_dict=True)
    
    class Meta:
        model = Product
        fields = [
            "product_Name",
            "price",
            "product_discriptions",
            "country",
        ]
