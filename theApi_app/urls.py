from django.urls import path
from .views import WeatherList, WeatherDetail

urlpatterns = [
    path('weather/', WeatherList.as_view(), name='weather-list'),
    path('weather/<int:pk>/', WeatherDetail.as_view(), name='weather-detail'),
]
