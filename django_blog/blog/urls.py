from django.urls import path
from . import views
from .views import (
    UserLoginView, UserLogoutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    register_view, profile_view, home_view
)

urlpatterns = [
    path("", home_view, name="home"),

  # CRUD routes
    path("posts/", PostListView.as_view(), name="posts"),           # list all posts
    path("post/new/", PostCreateView.as_view(), name="post-new"),   # create new post
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"), 
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # update
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # auth
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),

    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    path("search/", views.search_posts, name="search-posts"),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
