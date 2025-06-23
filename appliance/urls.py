from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import *
from core.views import *


urlpatterns = [
    path('', home, name="home"),
    path('book_service/', book_service, name="book_service"),
    path('pricing/', pricing, name="pricing"),
    path('reviews/', reviews, name="reviews"),
    path('about_us/', about_us, name="about_us"),
    path('booking_summary/<int:booking_id>/', booking_summary, name='booking_summary'),
    path('save-payment/', save_payment_info, name='save_payment'),
    path('submition/', submition, name="submition"),
    path('register/', register_view, name="register_view"),
    path('login/', login_view, name="login_view"),
    path('dashboard/', dashboard_view, name="dashboard_view"),
    path('logout/', logout_view, name="logout_view"),
    path('user_dashboard/', user_dashboard, name="user_dashboard"),
    path('edit-profile/', edit_profile_view, name='edit_profile'),
    path('change-password/', change_password_view, name='change_password'),
    path('bookings/', bookings_view, name='bookings_view'),
    path('booking/', book_service_view, name='booking'),
    path('my-bookings/', booking_list_view, name='booking_list'),
    path('edit-booking/<int:booking_id>/', edit_booking_view, name='edit_booking'),
    path('delete-booking/<int:booking_id>/', delete_booking_view, name='delete_booking'),


    path('admin/', admin.site.urls),
]

from core.views import booking_list_view, edit_booking_view, delete_booking_view

urlpatterns += [
    
]




from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


