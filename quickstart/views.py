from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer, CountriesSerializer
from .models import Product
from django_countries.data import COUNTRIES

def home(request):
    return render(request, template_name="home,html")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


class CountryView(viewsets.GenericViewSet):
    queryset = COUNTRIES
    serializer_class = CountriesSerializer
