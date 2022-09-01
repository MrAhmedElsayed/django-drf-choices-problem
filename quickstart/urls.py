from django.urls import path, include
from .views import home
from rest_framework import routers
from quickstart.views import ProductViewSet, countries_list


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("", home, name="home"),
    path('api/v1/', include(router.urls)),
    path('api/v1/countries_list/', countries_list),
]
