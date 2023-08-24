# CRUD
from flask import Flask, request, jsonify

app = Flask(__name__)

# DICTIONARY BOOKS
books = [
    {
        "id": 1,
        "name": "Lord of rings",
        "price": 100,
    },
    {
        "id": 2,
        "name": "Harry Potter",
        "price": 150
    },
    {
        "id": 3,
        "name": "Jammes Clear",
        "price": 120
    },
]


# READ
@app.route("/books", methods=["GET"])
def read_book():
    return jsonify(books)


# --------------------------------------------//------------------------------


# READ BY ID
@app.route("/books/<int:id>", methods=["GET"])
def read_by_id(id):
    for book in books:
        if book.get("id") == id:
            return jsonify(books)

# --------------------------------------------//--------------------------------


# Edit
@app.route("/books/<int:id>", methods=["PUT"])
def edit_book_by_id(id):
    altered_book = request.get_json()
    for indice, book in enumerate(books):
        if book.get("id") == id:
            books[indice].update(altered_book)
            return jsonify(books[indice])


# --------------------------------------------//----------------------------------


# create
@app.route("/books", methods=["POST"])
def create_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# ---------------------------------------------------//--------------------------------------------


# Delete
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_by_id(id):
    for indice, book in enumerate(books):
        if book.get("id") == id:
            del book[indice]
    return jsonify(books)


app.run(port=8080, host="localhost", debug=True)
