from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article

class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(publication_status=1).order_by("-publication_date")
    template_name = "index.html"
    paginate_by = 6

class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(publication_status=1)
        article = get_object_or_404(queryset, url_slug=slug)
        comments = article.comments.filter(approved=True).order_by("-publication_date")
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article_detail.html",
            {
                "article": article,  
                "comments": comments,
                "liked": liked
            },
        )
