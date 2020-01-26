from django.contrib import admin
from django.urls import path, include

from news.views import NewsListView

urlpatterns = [
    path('news/', include('news.urls', namespace='news')),
    path('user/', include('users.urls', namespace='user')),
    path('admin/', admin.site.urls),
    path('', NewsListView.as_view()),
]
