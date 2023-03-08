from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import books

urlpatterns = [
    path('', books, name='books')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

