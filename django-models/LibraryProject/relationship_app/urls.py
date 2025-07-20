# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs, useful for reverse lookups

urlpatterns = [
   path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]