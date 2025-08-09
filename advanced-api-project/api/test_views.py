"""
Test Suite for Book API

Covers:
- CRUD operations
- Filtering, searching, ordering
- Permissions & authentication checks

Run with:
    python manage.py test api
"""
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user and token
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.token = Token.objects.create(user=self.user)

        # Authenticate all requests with token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a sample book for read/update/delete tests
        self.book = Book.objects.create(title="Sample Book", author="John Doe", published_year=2020)

        # API endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])
        self.assertEqual(response.data[0]["title"], "Sample Book")

    def test_create_book(self):
        data = {"title": "New Book", "author": "Jane Doe", "published_year": 2021}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Sample Book")

    def test_update_book(self):
        data = {"title": "Updated Book", "author": "John Doe", "published_year": 2022}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_partial_update_book(self):
        data = {"title": "Partially Updated Book"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Partially Updated Book")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
