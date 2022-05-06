import os.path
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from fanbioware.settings import TEMPLATES_DIR
from .models import Game, News, Studio, Opening


def index(request):
    template = 'bioware/index.html'
    game_list = Game.objects.filter(is_released=True)
    news_list = News.objects.filter(is_publicated=True)[:4]
    openings = Opening.objects.all()
    roles_count = openings.count()
    teams_count = len(set([opening.team for opening in openings]))
    context = {
        'game_list': game_list,
        'news_list': news_list,
        'teams_count': teams_count,
        'roles_count': roles_count,
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
    template_path = os.path.join(TEMPLATES_DIR, f'bioware/{game_slug}.html')
    if os.path.isfile(template_path):
        template = f'bioware/{game_slug}.html'
    else:
        raise Http404()
    game = get_object_or_404(
        Game.objects.prefetch_related('news'),
        slug=game_slug
    )
    game_title = game.title
    next_game = Game.objects.exclude(id=game.id).last()
    news_list = game.news.all()[:]
    context = {
        'title': game_title,
        'game': game,
        'next_game': next_game,
        'news_list': news_list,
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
