from django.contrib import admin
from .models import Article, ArticleComment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('headline', 'url_slug', 'publication_status', 'publication_date')
    search_fields = ['headline', 'content_body']
    list_filter = ('publication_status', 'publication_date')
    prepopulated_fields = {'url_slug': ('headline',)}
    summernote_fields = ('content_body',)


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'comment_text', 'article', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('commenter_name', 'commenter_email', 'comment_text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)