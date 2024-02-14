from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pet.urls')),
    path("admin/", admin.site.urls),
]
