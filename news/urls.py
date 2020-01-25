from django.urls import path

from news.views import NewsCreateView, NewsListView, NewsDetailView, CommentView, NewsDeleteView, NewsUpdateView

app_name = 'news'

urlpatterns = [
    path('<int:pk>/comment/', CommentView.as_view(), name='comment'),
    path('<int:pk>/', NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='update'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('', NewsListView.as_view(), name='main'),
]
