from importlib import import_module

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .appsetting import APPS

static_urls = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
media_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = static_urls + media_urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

for app in APPS:
    try:
        mod = import_module(f'{app}.api')
    except:
        pass
    else:
        urlpatterns += [path('api/v1/', include((f'{app}.api', app), namespace='api/v1'))]
