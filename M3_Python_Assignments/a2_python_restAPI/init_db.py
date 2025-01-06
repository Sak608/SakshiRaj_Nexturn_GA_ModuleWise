import sqlite3

def init_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_year INTEGER NOT NULL,
        genre TEXT NOT NULL
    )
    """)

    # Sample Data
    sample_data = [
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction"),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Sci-Fi"),
    ]
    cursor.executemany("""
    INSERT INTO books (title, author, published_year, genre) 
    VALUES (?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()
    print("Database initialized and sample data added.")

if __name__ == "__main__":
    init_db()
