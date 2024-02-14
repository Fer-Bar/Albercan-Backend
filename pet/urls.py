from django.urls import path

from pet.views import main_page

urlpatterns = [
    path("index/", main_page, name="main_page"),
]
