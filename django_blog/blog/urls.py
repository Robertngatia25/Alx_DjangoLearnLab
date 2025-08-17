from django.urls import path
from .views import (
    UserLoginView, UserLogoutView,
    register_view, profile_view, home_view
)

urlpatterns = [
    path("", home_view, name="home"),

    # auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
