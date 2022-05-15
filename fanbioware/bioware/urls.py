from django.urls import path
from . import views

app_name = 'bioware'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('games/', views.GamesView.as_view(), name='game_list'),
    path(
        'games/<slug:game_slug>/',
        views.GameDetailView.as_view(),
        name='game_detail'
    ),
    path('careers/', views.CareersView.as_view(), name='careers'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]
