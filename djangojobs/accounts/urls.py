from django.urls import path, include
from .views import CustomUserView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'


urlpatterns = [
    path('', CustomUserView.as_view(), name='view'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token)
]
