from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {'id': 1, 'Artificial Intelligence': 'Book 1', 'Stuart Russell': 'Sebastian Thrun'},
    {'id': 2, 'Machine Learning': 'Book 2', 'Tom Mitchell': 'Trevor Hastie'},
    {'id': 3, 'Data Science': 'Book 3', 'Jake Porway': 'Hilary Mason'}
]


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = {'id': len(books) + 1, 'title': data['title'], 'author': data['author']}
    books.append(new_book)
    return jsonify(new_book), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(data)
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
