import os
import shutil
import tempfile
from http import HTTPStatus
from django.test import TestCase, Client
from django.test import Client, TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from fanbioware.utils import BIOWARE_URL_VS_TEMPLATE, create_test_template
from bioware.models import Game

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class URLTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
        cls.uploaded = SimpleUploadedFile(
            name='small.gif',
            content=cls.small_gif,
            content_type='image/gif'
        )

        cls.game = Game.objects.create(
            title='Test game',
            slug='mass-effect',
            description='Test game desc.',
            image=cls.uploaded,
            rel_date='2020-02-02',
        )
        cls.template_name = create_test_template(cls.game.slug)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        os.remove(cls.template_name)

    def setUp(self) -> None:
        self.guest_client = Client()

    def test_urls_exists_at_desired_location(self):
        """Checking the availability of pages to an anonymous user."""
        for url in BIOWARE_URL_VS_TEMPLATE:
            response = self.guest_client.get(url, follow=True)
            with self.subTest(response=response):
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pages_uses_correct_templates(self):
        """Checking that URLs use the appropriate templates."""
        for url, template in BIOWARE_URL_VS_TEMPLATE.items():
            response = self.guest_client.get(url)
            with self.subTest(response=response):
                self.assertTemplateUsed(response, template)
