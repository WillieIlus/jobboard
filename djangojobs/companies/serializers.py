from rest_framework import serializers

from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    location = serializers.StringRelatedField(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)  

    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'user', 'description', 'location', 'address', 'phone', 'website', 'logo', 'email', 'facebook', 'twitter', 'instagram', 'linkedin', 'url')
        read_only_fields = ('slug', 'user', 'url')