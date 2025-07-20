# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

app_name = 'relationship_app' # Namespace for URLs, useful for reverse lookups

urlpatterns = [
   path('books/', list_books, name='list_books'),
   path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
   path('login/', views.user_login, name='login'),
   path('logout/', views.user_logout, name='logout'),
   path('register/', views.register, name='register'),

]