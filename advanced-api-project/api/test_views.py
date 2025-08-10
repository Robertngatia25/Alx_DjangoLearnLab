from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from django.test.utils import override_settings

@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # In-memory test DB
    }
})
class BookAPITestCase(TestCase):
    def setUp(self):
        # Use DRF's APIClient
        self.client = APIClient()

        # Create test user and authenticate once
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

        # Example: Create a sample book for tests
        self.book_data = {
            'title': 'Test Book',
            'author': 'John Doe',
            'published_date': '2024-01-01',
            'isbn': '1234567890123',
            'price': '9.99'
        }

    def test_create_book(self):
        url = reverse('book-list')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        # Create a book
        self.client.post(reverse('book-list'), self.book_data, format='json')

        # Retrieve list
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
