from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'bioware'

urlpatterns = [
     path('', views.index, name='index'),
     path('about/', views.about, name='about'),
     path('games/', views.game_list, name='game_list'),
     path('games/<slug:game_slug>/', views.game_detail, name='game_detail'),
     path('careers/', views.careers, name='careers'),
     path('contacts/', views.contacts, name='contacts'),
]

if settings.DEBUG is True:
    urlpatterns += static(
         settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT
     )
