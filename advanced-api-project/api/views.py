from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

"""
BookListView:
- Supports filtering by: title, author name, publication_year
- Supports searching in: title, author name
- Supports ordering by: title, publication_year
Example usage:
    GET /books/?search=tolkien&ordering=-publication_year
"""
# List all books (read-only for unauthenticated users)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, Searching, and Ordering settings
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields (exact match)
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search fields (partial match)
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


# Retrieve one book by ID (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Create a new book (only authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update a book (only authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book (only authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
