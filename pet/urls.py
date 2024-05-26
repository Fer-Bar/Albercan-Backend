from django.urls import path

from pet.views import main_page

app_name = 'pet'
urlpatterns = [
    path("index/", main_page, name="main_page"),
]
