from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import books, book_info

urlpatterns = [
    path('', books, name='books'),
    path('<int:id>/', book_info, name='book-info'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

