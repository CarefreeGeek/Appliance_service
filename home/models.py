from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class ServiceBooking(models.Model):
    # Basic Information
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    customer_city = models.TextField(max_length=100, null=True, blank=True)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField(blank=True)
    appliance_name = models.CharField(max_length=100)
    problem_type = models.TextField()
    service_date = models.DateField()
    additional_info = models.TextField(blank=True, null=True)
    assigned = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_bookings')

    def __str__(self):
        return f"{self.customer_name} - {self.appliance_name} ({self.service_date})"
    
# models.py
class Payment(models.Model):
    booking = models.ForeignKey(ServiceBooking, on_delete=models.CASCADE)
    razorpay_payment_id = models.CharField(max_length=100)
    amount = models.FloatField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.full_name
    
