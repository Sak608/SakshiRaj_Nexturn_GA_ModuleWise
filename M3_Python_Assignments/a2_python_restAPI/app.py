from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the BookBuddy API! Use the available endpoints to manage your book collection."
    
# Database Helper Function
def db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn

# Add a new book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    published_year = data.get("published_year")
    genre = data.get("genre")

    if not title or not author or not published_year or not genre:
        return jsonify({"error": "Invalid data", "message": "All fields are required"}), 400

    try:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO books (title, author, published_year, genre) 
        VALUES (?, ?, ?, ?)
        """, (title, author, published_year, genre))
        conn.commit()
        return jsonify({"message": "Book added successfully", "book_id": cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({"error": "Database error", "message": str(e)}), 500
    finally:
        conn.close()

# Retrieve all books
@app.route("/books", methods=["GET"])
def get_books():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()

    return jsonify([dict(book) for book in books]), 200

# Retrieve a specific book by ID
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    book = cursor.fetchone()
    conn.close()

    if book:
        return jsonify(dict(book)), 200
    else:
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404

# Update a book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    published_year = data.get("published_year")
    genre = data.get("genre")

    if not title or not author or not published_year or not genre:
        return jsonify({"error": "Invalid data", "message": "All fields are required"}), 400

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE books SET title = ?, author = ?, published_year = ?, genre = ? WHERE id = ?
    """, (title, author, published_year, genre, id))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404

    conn.close()
    return jsonify({"message": "Book updated successfully"}), 200

# Delete a book
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Book not found", "message": "No book exists with the provided ID"}), 404

    conn.close()
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
