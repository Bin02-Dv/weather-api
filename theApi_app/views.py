from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Weather
from .serializers import WeatherSerializer

class WeatherList(generics.ListCreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class WeatherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

