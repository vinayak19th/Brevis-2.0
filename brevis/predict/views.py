from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Article

from .paper import get_articles

def index(request):
    hot_articles = get_articles()
    return render(request, 'predict/index.html', { "hot_articles" : hot_articles })


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_list'] = Article.objects.all()
        return context
        
    def get_object(self):
        obj = super().get_object()
        obj.summarize()
        return obj


