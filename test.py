import pytest
from flask import jsonify
from app import app, books

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Welcome to the Book API'

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert response.get_json() == books

def test_get_book(client):
    book_id = 1
    response = client.get(f'/books/{book_id}')
    assert response.status_code == 200
    expected_book = next((book for book in books if book['id'] == book_id), None)
    assert response.get_json() == expected_book

def test_get_nonexistent_book(client):
    book_id = 99
    response = client.get(f'/books/{book_id}')
    assert response.status_code == 404
    assert response.get_json() == {'error': 'Book not found'}
