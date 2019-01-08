from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article

# Create your views here.

class ArticleListView(ListView):
    template_name = 'articles/article_lists.html' #generic url: <blog>/<model_name>_list.html
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        print(self.kwargs)
        id_ = self.kwargs.get('id')
        obj = get_object_or_404(Article, id=id_)
        print(obj)
        return obj