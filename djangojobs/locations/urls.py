from django.urls import path

from .views import ( CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView, LocationListCreateAPIView, LocationRetrieveUpdateDestroyAPIView )

app_name = 'locations'

urlpatterns = [
    path('countries/<slug:slug>/', CountryRetrieveUpdateDestroyAPIView.as_view(), name='country-detail'),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list'),

    path('<slug:slug>/', LocationRetrieveUpdateDestroyAPIView.as_view(), name='location-detail'),
    path('', LocationListCreateAPIView.as_view(), name='location-list'),
]
