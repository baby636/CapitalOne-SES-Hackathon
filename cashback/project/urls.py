from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('coins', views.getCoins),
    path('mapData', views.getMapData)
]
