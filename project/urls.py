
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls')),
    path('laboratorio/', include('laboratorio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
