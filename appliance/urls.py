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
    path('admin/', admin.site.urls),
]



from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})


# urlpatterns = [
#     path('/', home, name="home"),
#     path('book_service/', book_service, name="book_service"),
#     path('booking_summary/<int:booking_id>/', booking_summary, name='booking_summary'),
#     path('/payment/<int:booking_id>/', start_payment, name='start_payment'),
#     path('/submition/', submition, name="submition"),
#     path('admin/', admin.site.urls),
# ]









if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


