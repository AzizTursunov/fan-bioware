from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path(
        'news/',
        views.NewsListView.as_view(),
        name='news_list'
    ),
    path(
        'news/<slug:category_slug>/',
        views.CategoryNewsListView.as_view(),
        name='category_news_list'
    ),
    path(
        'news/<slug:game_slug>/<int:news_pk>/',
        views.NewsDetailView.as_view(),
        name='news_detail'
    )
]
