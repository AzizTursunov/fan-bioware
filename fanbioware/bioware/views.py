import os.path
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView
from fanbioware.settings import TEMPLATES_DIR
from .models import Game, News, Studio, Opening


def index(request):
    template = 'bioware/index.html'
    game_list = Game.objects.all()
    news_list = News.objects.filter(is_publicated=True)[:4]
    openings = Opening.objects.values('team').annotate(
        roles_count=Count('role')
    )
    teams_count = openings.count()
    roles_count = openings.aggregate(Sum('roles_count'))
    context = {
        'game_list': game_list,
        'news_list': news_list,
        'teams_count': teams_count,
        'roles_count': roles_count.get('roles_count__sum', 0),
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


class AboutView(ListView):
    model = Studio
    template_name = 'bioware/about.html'
    extra_context = {'title': 'About'}


def game_list(request):
    template = 'bioware/game_list.html'
    game_list = Game.objects.all()
    context = {
        'game_list': game_list,
        'title': 'Our games'
    }
    return render(request, template, context)


class GamesView(ListView):
    model = Game
    template_name = 'bioware/game_list.html'

    def get_queryset(self):
        return Game.objects.filter(is_released=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our games'
        return context


def game_detail(request, game_slug):
    template_path = os.path.join(TEMPLATES_DIR, f'bioware/{game_slug}.html')
    if os.path.isfile(template_path):
        template = f'bioware/{game_slug}.html'
    else:
        raise Http404
    game_title = ' '.join(game_slug.split('-'))
    game = get_object_or_404(Game, slug=game_slug)
    next_game = Game.objects.exclude(id=game.id).last()
    news = News.objects.filter(game=game)[:4]
    main_news = news.first()
    news_list = news[1:]
    context = {
        'title': game_title,
        'game': game,
        'next_game': next_game,
        'main_news': main_news,
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


class CareersView(ListView):
    model = Opening
    template_name = 'bioware/careers.html'
    extra_context = {'title': 'Careers'}


def contacts(request):
    template = 'bioware/contacts.html'
    studio_list = Studio.objects.all()
    context = {
        'studio_list': studio_list,
        'title': 'Contacts'
    }
    return render(request, template, context)


class ContactsView(ListView):
    model = Studio
    template_name = 'bioware/contacts.html'
    extra_context = {'title': 'Contacts'}
