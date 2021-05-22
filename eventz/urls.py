from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

static_urls = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
media_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
] + static_urls + media_urls
