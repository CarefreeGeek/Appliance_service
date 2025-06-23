from django.contrib import admin

# Register your models here.
from .models import Employee, Booking, UserServiceBooking

admin.site.register(Employee)
admin.site.register(Booking)
admin.site.register(UserServiceBooking)