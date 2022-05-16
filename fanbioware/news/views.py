from django.views.generic import ListView, DetailView
from news.models import News


class NewsList(ListView):
    template = 'news/news.html'
    extra_context = {'title': 'News', 'text': 'This is news page'}
    # allow_empty = False

    def get_queryset(self):
        return News.objects.filter(is_publicated=True)


class NewsDetailView(DetailView):
    model = News
    pk_url_kwarg = 'news_pk'
