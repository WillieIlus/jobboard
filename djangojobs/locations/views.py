from django.shortcuts import render

from .models import Location
from .serializers import LocationSerializer, CountrySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LocationListCreateAPIView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'slug'

class LocationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'slug'
    
class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'

class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'
    