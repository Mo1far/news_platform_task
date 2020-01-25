from ckeditor.widgets import CKEditorWidget
from django import forms

from news.models import News, Comment


class NewsCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
