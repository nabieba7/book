from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Django Unleashed",
            "author": "Will Vincent",
            "isbn": "9781234567897",
            "description": "A powerful Django book",
            "published_date": "2020-01-01"
        }

    def test_create_book(self):
        response = self.client.post(reverse('api:book-list'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_books(self):
        self.client.post(reverse('api:book-list'), self.book_data, format='json')
        response = self.client.get(reverse('api:book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.post(reverse('api:book-list'), self.book_data, format='json')
        book_id = response.data['id']
        detail_url = reverse('api:book-detail', kwargs={'pk': book_id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
