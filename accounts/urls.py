from django.contrib.auth import views as django_views
from django.urls import path
from . import views

urlpatterns = [
    path(
        "login/",
        django_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("profile/", views.profile, name="profile"),
    path("logout/", django_views.LogoutView.as_view(), name="logout"),
]
