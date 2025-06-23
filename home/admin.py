from django.contrib import admin

# Register your models here.
from .models import ServiceBooking, Payment, Customer
admin.site.register(ServiceBooking)
admin.site.register(Payment)
admin.site.register(Customer)