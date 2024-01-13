from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS_CHOICES = [
    (0, 'Draft'),
    (1, 'Published'),
    (2, 'Archived'),
]


class Article(models.Model):
    headline = models.CharField(max_length=255, unique=True)
    url_slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authored_articles"
    )
    featured_image = CloudinaryField('image', default='default_image')
    summary = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    content_body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    publication_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    readers = models.ManyToManyField(
        User, related_name='liked_articles', blank=True)

    class Meta:
        ordering = ["-publication_date"]

    def __str__(self):
        return self.headline

    def number_of_readers(self):
        return self.readers.count()

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments")
    commenter_name = models.CharField(max_length=100)
    commenter_email = models.EmailField()
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment on '{self.article.headline}' by {self.commenter_name}"