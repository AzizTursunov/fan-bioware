from django.shortcuts import render
from .models import Game, News


def index(request):
    template = 'bioware/index.html'
    game_list = Game.objects.all()
    news_list = News.objects.all()[:4]
    context = {
        'game_list': game_list,
        'news_list': news_list
    }
    return render(request, template, context)


def about(request):
    template = 'bioware/about.html'
    return render(request, template)


def game_list(request):
    template = 'bioware/games.html'
    game_list = Game.objects.all()
    return render(request, template, {'game_list': game_list})


def game_detail(request):
    template = 'bioware/mass_effect.html'
    return render(request, template)


def careers(request):
    template = 'bioware/careers.html'
    return render(request, template)


def contacts(request):
    template = 'bioware/contacts.html'
    return render(request, template)
