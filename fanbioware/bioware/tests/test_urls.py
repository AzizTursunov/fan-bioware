from django.test import TestCase, Client
from http import HTTPStatus


class URLTest(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()
        self.urls_vs_templates = {
            '/': 'bioware/index.html',
            '/about/': 'boiware/about.html',
            '/games/': 'bioware/games.html',
            '/games/mass_effect/': 'bioware/mass_effect.html',
            '/careers/': 'bioware/careers.html',
            '/contacts/': 'bioware/contacts.html'
        }

    def test_urls_exists_at_desired_location(self):
        """Checking the availability of pages to an anonymous user."""
        for url in self.urls_vs_templates:
            response = self.guest_client.get(url)
            with self.subTest(response=response):
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pages_uses_correct_templates(self):
        """Checking that URLs use the appropriate templates."""
        for url, template in self.urls_vs_templates.items():
            response = self.guest_client.get(url)
            with self.subTest(response=response):
                self.assertTemplateUsed(response, template)
