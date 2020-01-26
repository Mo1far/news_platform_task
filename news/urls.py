from django.urls import path

from news.views import NewsCreateView, NewsListView, NewsDetailView, CommentView, NewsDeleteView, NewsUpdateView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='main'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='delete'),
    path('<int:pk>/comment/', CommentView.as_view(), name='comment'),
]
