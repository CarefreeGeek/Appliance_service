from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserServiceBookingForm, EditProfileForm, ChangePasswordForm
from .models import UserServiceBooking
from core.models import Booking
from home.models import ServiceBooking
from core.middlewares import auth, guest


@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render (request,'auth/user_dashboard.html')
    else:
        initial_data = {'username':'', 'first_name':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard_view')
        else:
            errr = "Invalid username or password"
            return render(request, 'auth/login.html',{'form':form, 'error':'error'})
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@auth
def dashboard_view(request):
    context = {
        'user': request.user,
        'bookings_count': ServiceBooking.objects.filter(user=request.user).count()
    }
    return render(request, 'auth/user_dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')


def mac_dashboard(request):
    return render(request, 'auth/mac_dashboard.html')

def bookings_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'auth/bookings.html', {'bookings': bookings})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('dashboard_view')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'auth/edit_profile.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            if not user.check_password(form.cleaned_data['current_password']):
                form.add_error('current_password', 'Current password is incorrect.')
            else:
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password changed successfully.")
                return redirect('dashboard_view')
    else:
        form = ChangePasswordForm()
    return render(request, 'auth/change_password.html', {'form': form})

@login_required
def book_service_view(request):
    if request.method == 'POST':
        form = UserServiceBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookings_view')  # Or confirmation page
    else:
        initial_address = ''
        if hasattr(request.user, 'customer'):
            initial_address = request.user.customer.address

        form = UserServiceBookingForm(initial={'address': initial_address})
    
    return render(request, 'auth/booking.html', {'form': form, 'user': request.user})






@login_required
def booking_list_view(request):
    bookings = ServiceBooking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'auth/booking_list.html', {'bookings': bookings})


@login_required
def edit_booking_view(request, booking_id):
    booking = get_object_or_404(ServiceBooking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.customer_name = request.POST.get('customer_name')
        booking.customer_address = request.POST.get('customer_address')
        booking.customer_city = request.POST.get('customer_city')
        booking.customer_phone = request.POST.get('customer_phone')
        booking.customer_email = request.POST.get('customer_email')
        booking.appliance_name = request.POST.get('appliance_name')
        booking.problem_type = request.POST.get('problem_type')
        booking.service_date = request.POST.get('service_date')
        booking.additional_info = request.POST.get('additional_info')
        booking.save()
        return redirect('booking_list')

    return render(request, 'auth/edit_booking.html', {'booking': booking})


@login_required
def delete_booking_view(request, booking_id):
    booking = get_object_or_404(ServiceBooking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return HttpResponseForbidden("You can't delete this")



