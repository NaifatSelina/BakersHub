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
        comments = article.comments.filter(is_approved=True).order_by("-created_at")
        liked = request.user in article.readers.all()

        return render(
            request,
            "article_detail.html",
            {
                "article": article,  
                "comments": comments,
                "liked": liked
            },
        )
