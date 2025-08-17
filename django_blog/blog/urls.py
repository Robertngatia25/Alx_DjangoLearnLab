from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    register_view, profile_view, home_view
)

urlpatterns = [
    path("", home_view, name="home"),

  # CRUD routes
    path("posts/", PostListView.as_view(), name="posts"),              # list
    path("posts/new/", PostCreateView.as_view(), name="post-create"),  # create
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # detail
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # update
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
