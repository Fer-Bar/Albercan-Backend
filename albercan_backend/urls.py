from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pet.urls', namespace='pet')),
    path('', include('people.urls', namespace='people')),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
