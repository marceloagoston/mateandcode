from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('cuentas/', include('accounts.urls')), #in this case the order matters. 'cause dj reads top-to-bot
    path('', include('blog.urls')),
]
