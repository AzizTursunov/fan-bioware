from django.test import Client, TestCase
from ..configs import REVERSE_URL_VS_TEMPLATE


class BiowareViewsTest(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_bioware_pages_uses_correct_templates(self):
        """Checking that URLs use the appropriate templates."""

        for reverse_name, template in REVERSE_URL_VS_TEMPLATE.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
