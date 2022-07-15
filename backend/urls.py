from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
