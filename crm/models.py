from django.db import models

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.FloatField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
