from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm
# Create your views here.

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html' #generic url: <blog>/<model_name>_list.html
    form_class = ArticleModelForm

class ArticleListView(ListView):
    template_name = 'articles/article_lists.html' #generic url: <blog>/<model_name>_list.html
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        print(id_)
        obj = get_object_or_404(Article, id=id_)
        return obj

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html' #generic url: <blog>/<model_name>_list.html
    form_class = ArticleModelForm
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        print(id_)
        obj = get_object_or_404(Article, id=id_)
        return obj

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html' #generic url: <blog>/<model_name>_list.html
    form_class = ArticleModelForm
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        print(id_)
        obj = get_object_or_404(Article, id=id_)
        obj.delete
        return obj

    def get_success_url(self):
        return reverse('articles:article-list')