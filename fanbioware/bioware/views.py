import os.path
from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView
from fanbioware.settings import TEMPLATES_DIR
from .models import Game, Studio, Opening
from news.models import News


class IndexView(TemplateView):
    template_name = 'bioware/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_list'] = Game.objects.filter(is_released=True)
        context['news_list'] = News.objects.filter(
            is_publicated=True
        )[:4].select_related('game')
        openings = Opening.objects.all()
        context['roles_count'] = openings.count()
        context['teams_count'] = len(
            set([opening.team for opening in openings])
        )
        context['title'] = 'Bioware'
        return context


class AboutView(ListView):
    model = Studio
    template_name = 'bioware/about.html'
    extra_context = {'title': 'About'}


class GamesView(ListView):
    model = Game
    template_name = 'bioware/game_list.html'

    def get_queryset(self):
        return Game.objects.filter(is_released=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our games'
        return context


class GameDetailView(DetailView):
    model = Game
    slug_url_kwarg = 'game_slug'
    allow_empty = False

    def get_queryset(self):
        return super(
            GameDetailView,
            self
        ).get_queryset().prefetch_related('news', 'slider')

    def get_template_names(self):
        templates = []
        template_path = os.path.join(
            TEMPLATES_DIR, f'bioware/{self.object.slug}.html'
        )
        if not os.path.isfile(template_path):
            raise Http404
        templates.append(f'bioware/{self.object.slug}.html')
        return templates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next_game = Game.objects.exclude(id=self.object.id).last()
        context['title'] = self.object.slug.split('-')
        context['next_game'] = next_game
        return context


class CareersView(ListView):
    model = Opening
    template_name = 'bioware/careers.html'
    extra_context = {'title': 'Careers'}

    def get_queryset(self):
        return Opening.objects.select_related('studio').all()


class ContactsView(ListView):
    model = Studio
    template_name = 'bioware/contacts.html'
    extra_context = {'title': 'Contacts'}

    def get_queryset(self):
        return Studio.objects.prefetch_related('slider').all()
