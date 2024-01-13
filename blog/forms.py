from .models import ArticleComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['comment_text',]