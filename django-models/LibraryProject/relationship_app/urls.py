# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from . import views # Import views from the current app

app_name = 'relationship_app' # Namespace for URLs, useful for reverse lookups

urlpatterns = [
    # URL for the function-based view: lists all books
    # Example URL: /relationships/books/
    path('books/', views.book_list, name='book_list'),

    # URL for the class-based view: displays details for a specific library
    # <int:pk> is a path converter that captures an integer (primary key)
    # Example URL: /relationships/libraries/1/
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]