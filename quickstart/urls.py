from django.urls import path, include
from .views import home
from rest_framework import routers
from quickstart.views import ProductViewSet, CountryView


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
# router.register(r'country', CountryView)

urlpatterns = [
    path("", home, name="home"),
    path('api/v1/', include(router.urls)),
]
