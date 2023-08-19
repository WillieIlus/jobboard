from django.urls import path

from .views import CategoryList, CategoryDetail

app_name = 'categories'

urlpatterns = [
    path('', CategoryList.as_view(), name='list'),
    path('<slug:slug>/', CategoryDetail.as_view(), name='detail'),
]
