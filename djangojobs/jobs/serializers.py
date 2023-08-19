from rest_framework import serializers

from .models import Job, Impression, Click


class JobSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='author.username', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_email = serializers.CharField(source='company.email', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    timesince = serializers.CharField(source='timeSince', read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    job_type = serializers.CharField(source='get_job_type', read_only=True)


    class Meta:
        model = Job
        fields = (
            'id', 'author', 'user_name', 'email', 'user_email', 'company', 'company_name', 
            'company_email', 'job_type', 'location', 'location_name', 'category', 'category_name',
            'title', 'slug', 'description', 'experience', 'salary', 'created_at', 'updated_at', 'active', 
            'timesince',  'featured', 'url',  'salary', 'paid', 'paid_at',
            'paid_amount', 'phone_number', 'url', 'days_left', 'expires_soon', 'is_expired', 'job_type'

        )
        extra_kwargs = {'last_date': {'read_only': True}}


class ImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impression
        fields = ('id', 'job', 'source_ip', 'session_id', 'timestamp')


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ('id', 'job', 'source_ip', 'session_id', 'timestamp')
