from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView, DetailView, FormView, DeleteView, UpdateView

from news.forms import NewsCreateForm, CommentForm
from news.models import News, Comment
from users.sendgridAPI import SendGridAPI


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsCreateForm
    template_name = 'news/news_create.html'
    success_url = '/news/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.instance.author.has_perm('news.publish'):
            form.instance.status = 'PUBLISHED'
        return super().form_valid(form)


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news/'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user and not self.request.user.has_perm('news:can_delete'):
            raise PermissionDenied('You are dont have permissions for this')
        return super(NewsDeleteView, self).delete(request, *args, **kwargs)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        comments = Comment.objects.filter(post=self.object)
        context['comments'] = comments
        context['can_delete'] = self.request.user.has_perm(
            'news.delete_news') or self.request.user == self.object.author
        context['can_change'] = self.request.user.has_perm(
            'news.change_news') or self.request.user == self.object.author

        return context


class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'content')
    template_name_suffix = '_update'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user or request.user.has_perm('can_edit'):
            raise PermissionDenied()
        return super(NewsUpdateView, self).dispatch(request, *args, **kwargs)


class NewsListView(ListView):
    queryset = News.objects.filter(status='PUBLISHED')
    template_name = 'news/home.html'
    context_object_name = 'news_list'
    ordering = '-posted_date'
    paginate_by = 3


class CommentView(FormView):
    model = News
    form_class = CommentForm
    success_url = '/news/'

    def form_valid(self, form):
        news = News.objects.get(id=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = news
        comment = form.save()
        SendGridAPI.send_new_comment_notification_mail(comment.post.author, comment, self.request)
        return super().form_valid(form)
