from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('categories/', include('categories.urls', namespace='categories')),
    path('companies/', include('companies.urls', namespace='companies')),
    path('locations/', include('locations.urls', namespace='locations')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('api-auth/', include('rest_framework.urls'))
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
