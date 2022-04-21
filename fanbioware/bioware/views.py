from django.shortcuts import get_object_or_404, render
from .models import Game, News, Studio, Opening


def index(request):
    template = 'bioware/index.html'
    game_list = Game.objects.all()
    news_list = News.objects.filter(is_publicated=True)[:4]
    context = {
        'game_list': game_list,
        'news_list': news_list,
        'title': 'Bioware'
    }
    return render(request, template, context)


def about(request):
    template = 'bioware/about.html'
    studio_list = Studio.objects.all()
    context = {
        'studio_list': studio_list,
        'title': 'About'
    }
    return render(request, template, context)


def game_list(request):
    template = 'bioware/games.html'
    game_list = Game.objects.all()
    context = {
        'game_list': game_list,
        'title': 'Our games'
    }
    return render(request, template, context)


def game_detail(request, game_slug):
    template = f'bioware/{game_slug}.html'
    game_title = ' '.join([word.capitalize() for word in game_slug.split('-')])
    game = get_object_or_404(Game, slug=game_slug)
    news = News.objects.filter(game=game)[:4]
    main_news = news.first()
    news_list = news[1:]
    context = {
        'title': game_title,
        'game': game,
        'main_news': main_news,
        'news_list': news_list
    }
    return render(request, template, context)


def careers(request):
    template = 'bioware/careers.html'
    opening_list = Opening.objects.all()
    context = {
        'opening_list': opening_list,
        'title': 'Careers'
    }
    return render(request, template, context)


def contacts(request):
    template = 'bioware/contacts.html'
    studio_list = Studio.objects.all()
    context = {
        'studio_list': studio_list,
        'title': 'Contacts'
    }
    return render(request, template, context)
