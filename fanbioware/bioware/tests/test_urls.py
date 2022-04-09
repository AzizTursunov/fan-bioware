from django.test import TestCase, Client
from http import HTTPStatus
from fanbioware.utils import BIOWARE_URL_VS_TEMPLATE


class URLTest(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_urls_exists_at_desired_location(self):
        """Checking the availability of pages to an anonymous user."""
        for url in BIOWARE_URL_VS_TEMPLATE:
            response = self.guest_client.get(url)
            with self.subTest(response=response):
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pages_uses_correct_templates(self):
        """Checking that URLs use the appropriate templates."""
        for url, template in BIOWARE_URL_VS_TEMPLATE.items():
            response = self.guest_client.get(url)
            with self.subTest(response=response):
                self.assertTemplateUsed(response, template)
