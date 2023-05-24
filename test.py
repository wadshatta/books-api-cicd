import unittest
from flask import Flask, jsonify

# Import the Flask application and books data
from app import app, books


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome to the Book API')

    def test_get_books(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), books)

    def test_get_book(self):
        book_id = 1
        response = self.client.get(f'/books/{book_id}')
        self.assertEqual(response.status_code, 200)
        expected_book = next((book for book in books if book['id'] == book_id), None)
        self.assertEqual(response.get_json(), expected_book)

    def test_get_nonexistent_book(self):
        book_id = 99
        response = self.client.get(f'/books/{book_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'error': 'Book not found'})


if __name__ == '__main__':
    unittest.main()
