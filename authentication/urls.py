from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from authentication.forms import UserLoginForm

app_name = "authentication"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="authentication/login_page.html", form_class=UserLoginForm
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]
