from django.urls import path
from . import views

app_name = 'bioware'

urlpatterns = [
     path('', views.index, name='index'),
     path('about/', views.about, name='about'),
     path('games/', views.game_list, name='game_list'),
     path('games/mass_effect/', views.game_detail, name='game_detail'),
     path('careers/', views.careers, name='careers'),
     path('contacts/', views.contacts, name='contacts'),
]
