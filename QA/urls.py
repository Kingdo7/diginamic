from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    #path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

