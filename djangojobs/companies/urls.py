# create urls for the companies appviews

from django.urls import path
from .views import CompanyListCreateAPIView, CompanyRetrieveUpdateDestroyAPIView

app_name = 'companies'

urlpatterns = [
    path('', CompanyListCreateAPIView.as_view(), name='list'),
    path('<slug:slug>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
]
