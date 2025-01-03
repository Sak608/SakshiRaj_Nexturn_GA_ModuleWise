# from customer_management import Customer 

# class Transaction(Customer):
#     def __init__(self, name, email, phone, book_title, quantity_sold):
#         super().__init__(name, email, phone)
#         self.book_title = book_title
#         self.quantity_sold = quantity_sold

#     def display(self):
#         return f"Customer: {self.name}, Book: {self.book_title}, Quantity Sold: {self.quantity_sold}"

# sales = []

# def sell_book(customer_name, email, phone, book_title, quantity):
#     from book_management import books 

#     try:
#         quantity = int(quantity)
#         if quantity <= 0:
#             raise ValueError("Quantity must be a positive number.")

#         for book in books:
#             if book.title.lower() == book_title.lower():
#                 if book.quantity >= quantity:
#                     book.quantity -= quantity
#                     sales.append(Transaction(customer_name, email, phone, book.title, quantity))
#                     return f"Sale successful! Remaining quantity: {book.quantity}"
#                 else:
#                     return f"Error: Only {book.quantity} copies available. Sale cannot be completed."
#         return "Error: Book not found."
#     except ValueError as e:
#         return f"Error: {e}"

# def view_sales():
#     if not sales:
#         return "No sales records found."
#     return "\n".join([sale.display() for sale in sales])                        

class SalesManager:
    def __init__(self):
        self.sales = []

    def sell_book(self, book_title, quantity, customer_name):
        # Add your logic to handle book sale and reduce quantity
        # For now, let's assume the sale is successful
        self.sales.append({'book_title': book_title, 'quantity': quantity, 'customer_name': customer_name})
        return True, "Sale successful!"

    def view_sales(self):
        return self.sales
