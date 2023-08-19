from rest_framework import serializers
from .models import Country, Location

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'slug', 'code', 'flag')

class LocationSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Location
        fields = ('id', 'name', 'slug', 'country', 'flag')
