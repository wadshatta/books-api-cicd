from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
books = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1',
    },
    {
        'id': 2,
        'title': 'Book 2',
        'author': 'Author 2',
    },
    {
        'id': 3,
        'title': 'Book 3',
        'author': 'Author 3',
    }
]

# Routes
@app.route('/')
def home():
    return 'Welcome to the Book API'

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)
    
