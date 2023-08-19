from django.shortcuts import render
from rest_framework import generics, permissions, mixins, viewsets
# create list, create, update, delete, detail, search, filter, sort, and more

from .models import Company
from .serializers import CompanySerializer

class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    lookup_field = 'slug'
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    search_fields = ['name', 'description', 'address', 'phone', 'website', 'email', 'facebook', 'twitter', 'instagram', 'linkedin']
    filter_fields = ['name', 'description', 'address', 'phone', 'website', 'email', 'facebook', 'twitter', 'instagram', 'linkedin']
    ordering_fields = ['name', 'description', 'address', 'phone', 'website', 'email', 'facebook', 'twitter', 'instagram', 'linkedin']


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    lookup_field = 'slug'
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


   

