from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for books, customers, and sales
books = []
customers = []
sales = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET', 'POST'])
def books_page():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        books.append({'title': title, 'author': author, 'price': price, 'quantity': quantity})
    return render_template('books.html', books=books)

@app.route('/customers', methods=['GET', 'POST'])
def customers_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        customers.append({'name': name, 'email': email, 'phone': phone})
    return render_template('customers.html', customers=customers)

@app.route('/sales', methods=['GET', 'POST'])
def sales_page():
    sales_summary = {'books': [], 'quantities': []}
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        book_title = request.form['book_title']
        quantity = int(request.form['quantity'])

        # Update book stock and log the sale
        for book in books:
            if book['title'] == book_title:
                if book['quantity'] >= quantity:
                    book['quantity'] -= quantity
                    sales.append({'customer': customer_name, 'book': book_title, 'quantity': quantity})
                else:
                    return "Error: Not enough stock!"
                break

    # Prepare sales summary
    for sale in sales:
        if sale['book'] not in sales_summary['books']:
            sales_summary['books'].append(sale['book'])
            sales_summary['quantities'].append(sale['quantity'])
        else:
            index = sales_summary['books'].index(sale['book'])
            sales_summary['quantities'][index] += sale['quantity']

    return render_template('sales.html', sales=sales, sales_summary=sales_summary)

if __name__ == '__main__':
    app.run(debug=True)
