from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from django_countries.data import COUNTRIES
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return render(request, template_name="home,html")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


@api_view(['GET'])
def countries_list(request):
    return Response(COUNTRIES)
