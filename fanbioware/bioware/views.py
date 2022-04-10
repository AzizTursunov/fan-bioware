from django.shortcuts import get_object_or_404, render
from .models import Game, News, Studio


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


def game_detail(request, game_slug):
    template = f'bioware/{game_slug}.html'
    return render(request, template)


def careers(request):
    template = 'bioware/careers.html'
    studio_list = Studio.objects.prefetch_related('openings').all()
    return render(request, template, {'studio_list': studio_list})


def contacts(request):
    template = 'bioware/contacts.html'
    studio_list = Studio.objects.all()
    return render(request, template, {'studio_list': studio_list})
