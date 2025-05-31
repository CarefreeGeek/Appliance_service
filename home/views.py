from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from home.models import Payment, ServiceBooking, Customer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from core.views import user_dashboard

# Create your views here.
def home(request):
    return render(request, 'main/home.html')



def book_service(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        if not customer_name:
            return HttpResponse("Customer name is required", status=400)
        # Baaki fields ka bhi check kar sakte hain yahan

        booking = ServiceBooking.objects.create(
            customer_name=customer_name,
            customer_address=request.POST.get('customer_address', ''),
            customer_city=request.POST.get('customer_city', ''),
            customer_phone=request.POST.get('customer_phone', ''),
            customer_email=request.POST.get('customer_email', ''),
            appliance_name=request.POST.get('appliance_name', ''),
            problem_type=request.POST.get('problem_type', ''),
            service_date=request.POST.get('service_date'),
            additional_info=request.POST.get('additional_info', '')
        )
        return redirect('booking_summary', booking_id=booking.id)
    return render(request, 'main/book.html')



def booking_summary(request, booking_id):
    booking = get_object_or_404(ServiceBooking, id=booking_id)
    return render(request, 'main/booking_summary.html', {
        'booking': booking,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID
    })

@csrf_exempt
def save_payment_info(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id')
        booking_id = request.POST.get('booking_id')
        amount = request.POST.get('amount')

        booking = ServiceBooking.objects.get(id=booking_id)

        Payment.objects.create(
            booking=booking,
            razorpay_payment_id=payment_id,
            amount=amount,
            status='Success'
        )

        return JsonResponse({'status': 'saved'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def submition(request):
    return render(request, 'main/submission.html')






def pricing(request):
    return render(request, 'main/pricing.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def about_us(request):
    return render(request, 'main/about_us.html')


def user_dashboard(request):
    return render(request, 'main/user_dashboard.html')



# def user_dashboard(request):
#     if request.method == 'GET':
#         customer = Customer.objects.get(email=request.user.email)
#         return render(request, 'main/user_dashboard.html', {'customer': customer})
#     else:
#         return render(request, 'main/user_login.html', {'error': 'Something went wrong'})

