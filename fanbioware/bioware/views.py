from django.shortcuts import render


def index(request):
    template = 'bioware/index.html'
    return render(request, template)


def about(request):
    template = 'bioware/about.html'
    return render(request, template)


def game_list(request):
    template = 'bioware/games.html'
    return render(request, template)


def game_detail(request):
    template = 'bioware/mass_effect.html'
    return render(request, template)


def careers(request):
    template = 'bioware/careers.html'
    return render(request, template)


def contacts(request):
    template = 'bioware/contacts.html'
    return render(request, template)
