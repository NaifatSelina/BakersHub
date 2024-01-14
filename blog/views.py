from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article
from .forms import CommentForm

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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(publication_status=1)
        article = get_object_or_404(queryset, url_slug=slug)
        comments = article.comments.filter(is_approved=True).order_by("-created_at")
        liked = request.user in article.readers.all()

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_detail.html",
            {
                "article": article,  
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    
class ArticleLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, url_slug=slug)
        
        if article.readers.filter(id=request.user.id).exists():
            article.readers.remove(request.user)
        else:
            article.readers.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))

