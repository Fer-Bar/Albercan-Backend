from django.urls import path

from people.views import PersonListView

app_name = "people"
urlpatterns = [
    path("members/", PersonListView.as_view(), name="member-list"),
]
