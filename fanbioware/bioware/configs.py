from django.urls import reverse

URL_VS_TEMPLATE = {
    '/': 'bioware/index.html',
    '/about/': 'boiware/about.html',
    '/games/': 'bioware/games.html',
    '/games/mass_effect/': 'bioware/mass_effect.html',
    '/careers/': 'bioware/careers.html',
    '/contacts/': 'bioware/contacts.html'
}

REVERSE_URL_VS_TEMPLATE = {
    reverse('bioware:index'): 'bioware/index.html',
    reverse('bioware:about'): 'boiware/about.html',
    reverse('bioware:game_list'): 'bioware/games.html',
    reverse('bioware:game_detail'): 'bioware/mass_effect.html',
    reverse('bioware:careers'): 'bioware/careers.html',
    reverse('bioware:contacts'): 'bioware/contacts.html'
}
