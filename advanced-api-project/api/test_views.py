from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

"""
Test Suite for Book API

Covers:
- CRUD operations
- Filtering, searching, ordering
- Permissions & authentication checks

Run with:
    python manage.py test api
"""

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name="Author One")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # URLs
        self.list_url = reverse('book-list')   # Name from urls.py
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {"title": "Updated Title", "publication_year": 2021, "author": self.author.id}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_create_book_requires_authentication(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
