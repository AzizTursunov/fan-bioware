from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from news.models import News
from bioware.models import Game


class NewsListView(ListView):
    template = 'news/news_list.html'
    extra_context = {'title': ['News']}
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(is_publicated=True)


class CategoryNewsListView(ListView):
    model = News
    template = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        slug = self.kwargs.get('category_slug')
        if slug != 'bioware':
            news = get_object_or_404(
                Game.objects.prefetch_related('news'),
                slug=slug
            ).news.filter(is_publicated=True)
            return news
        news = News.objects.filter(game=None, is_publicated=True)
        return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('category_slug').split('-')
        return context


class NewsDetailView(DetailView):
    model = News
    template = 'news/news_detail.html'
    pk_url_kwarg = 'news_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['news'].title
        return context
