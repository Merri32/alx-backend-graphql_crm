import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_graphql_crm.settings")
django.setup()

from crm.models import Customer, Product, Order

# Clear existing data
Order.objects.all().delete()
Product.objects.all().delete()
Customer.objects.all().delete()

# Seed Customers
customers = [
    {"name": "Alice", "email": "alice@example.com", "phone": "+1234567890"},
    {"name": "Bob", "email": "bob@example.com", "phone": "123-456-7890"},
    {"name": "Carol", "email": "carol@example.com"},
]

for c in customers:
    Customer.objects.create(**c)

# Seed Products
products = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Phone", "price": 499.99, "stock": 20},
    {"name": "Tablet", "price": 299.99, "stock": 15},
]

for p in products:
    Product.objects.create(**p)

# Seed Orders
customer1 = Customer.objects.get(email="alice@example.com")
customer2 = Customer.objects.get(email="bob@example.com")
product1 = Product.objects.get(name="Laptop")
product2 = Product.objects.get(name="Phone")

order1 = Order.objects.create(customer=customer1)
order1.products.set([product1, product2])
order1.total_amount = product1.price + product2.price
order1.save()

order2 = Order.objects.create(customer=customer2)
order2.products.set([product2])
order2.total_amount = product2.price
order2.save()

print("Database seeded successfully!")
