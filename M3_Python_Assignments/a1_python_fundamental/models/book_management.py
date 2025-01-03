# class Book:
#     def __init__(self, title, author, price, quantity):
#         self.title = title
#         self.author = author 
#         self.price = price 
#         self.quantity = quantity 

#     def display(self):
#         return f"{self.title} by {self.author}, Price: {self.price}, Quantity: {self.quantity}"

# books = []

# def add_book(title, author, price, quantity):
#     try:
#         price = float(price)
#         quantity = int(quantity)
#         if price <= 0 or quantity <= 0:
#             raise valueError("Price and quantity must be positive numbers.")
#         books.append(Book(title, author, price, quantity))
#         return "Book added successfully!"
#     except ValueError as e:
#         return f"Error: {e}"

# def view_books():
#     if not books: 
#         return "No books available."
#     return "\n".join([book.display() for book in books])

# def search_book(keyword):
#     results = [book for book in books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
#     return "\n".join([book.display() for book in results]) if results else "No matching books found."    

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price, quantity):
        self.books.append({'title': title, 'author': author, 'price': price, 'quantity': quantity})

    def view_books(self):
        return self.books
