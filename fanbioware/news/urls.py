from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path(
        'news/',
        views.NewsList.as_view(),
        name='news_list'
    ),
    path(
        'news/<int:news_pk>/',
        views.NewsDetailView.as_view(),
        name='news_detail'
    )
]
