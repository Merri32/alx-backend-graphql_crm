import re
import graphene
from graphene_django import DjangoObjectType
from graphene import Mutation, String, Field
from .models import Customer

# -------------------------
# CustomerType with Meta class
# -------------------------
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "email", "phone")

# -------------------------
# Query class
# -------------------------
class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()

# -------------------------
# CreateCustomer Mutation
# -------------------------
class CreateCustomer(Mutation):
    customer = Field(lambda: CustomerType)
    message = String()

    class Arguments:
        name = String(required=True)
        email = String(required=True)
        phone = String(required=False)

    def mutate(root, info, name, email, phone=None):
        # Check for duplicate email
        if Customer.objects.filter(email=email).exists():
            raise Exception("Email already exists")

        # Optional phone validation
        if phone:
            phone_pattern = re.compile(r'^(\+\d{10,15}|\d{3}-\d{3}-\d{4})$')
            if not phone_pattern.match(phone):
                raise Exception("Invalid phone format")

        customer = Customer(name=name, email=email, phone=phone)
        customer.save()

        return CreateCustomer(customer=customer, message="Customer created successfully")

# -------------------------
# Mutation container
# -------------------------
class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
