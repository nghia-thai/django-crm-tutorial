from django.shortcuts import render
from rest_framework import generics

from customer.models import Customer
from customer.serializers import CustomerSerializer

# Create your views here.
class CustomerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class Customerlist(generics.ListAPIView):
    # API endpoint that allows customer to be viewed
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDelete(generics.RetrieveDestroyAPIView):
    # API endpoints that allows a customer record to be deleted
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
