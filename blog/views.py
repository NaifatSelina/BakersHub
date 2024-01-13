from django.shortcuts import render
from django.views import generic
from .models import Article

class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(publication_status=1).order_by("-publication_date")
    template_name = "index.html"
    paginate_by = 6

