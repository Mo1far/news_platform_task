from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('news/', include('news.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]
