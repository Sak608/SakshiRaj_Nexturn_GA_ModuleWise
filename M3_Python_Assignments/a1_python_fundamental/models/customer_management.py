# class Customer:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email 
#         self.phone = phone 

#     def display(self):
#         return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

# customers = []

# def add_customer(name, email, phone):
#     if not name or not email or not phone:
#         return "Error: All fields are required."
#     customers.append(Customer(name, email, phone))
#     return "Customer added successfully!" 

# def view_customers():
#     if not customers:
#         return "No customers found."
#     return "\n".join([customer.display() for customer in customers])           


class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email, phone):
        self.customers.append({'name': name, 'email': email, 'phone': phone})

    def view_customers(self):
        return self.customers
