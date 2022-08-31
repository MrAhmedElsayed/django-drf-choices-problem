from collections import defaultdict
from .models import Product
from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from django_countries import Countries
from django_countries.data import COUNTRIES

# print(COUNTRIES)



class CountriesSerializer(serializers.ChoiceField):
    
    def get_countries(self):
        return COUNTRIES

        
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