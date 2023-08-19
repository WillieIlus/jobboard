from django.urls import path
from .views import JobListCreateAPIView, JobRetrieveUpdateDestroyAPIView 

app_name = 'jobs'

urlpatterns = [
    path('', JobListCreateAPIView.as_view(), name='list'),
    path('<slug:slug>/', JobRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
]
