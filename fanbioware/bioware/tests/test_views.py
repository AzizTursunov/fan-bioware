
import shutil
import tempfile
from django.urls import reverse
from django.test import Client, TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from fanbioware.utils import BIOWARE_REVERSE_URL_VS_TEMPLATE, NEWS_ON_PAGE
from ..models import Game, News, Openings

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class BiowareViewsTest(TestCase):
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

        cls.game_list = []
        for i in range(1, 5):
            cls.game_list.append(
                Game(
                    pk=i,
                    title=f'Test game #{i}',
                    description=f'Test desc for game #{i}.',
                    image=cls.uploaded,
                    platforms='Xbox',
                    release_date='2020-02-02',
                    genre='Action'
                )
            )
        Game.objects.bulk_create(cls.game_list)
        cls.games = Game.objects.all()
        cls.news_list = []
        for i in range(NEWS_ON_PAGE):
            cls.news_list.append(
                News(
                    game=Game.objects.get(pk=1),
                    title='Test news title for game #1',
                    intro='Test news intro for game #1.',
                    text='Test news text for game #1.',
                    image=cls.uploaded,
                    tags='Test news tags.'
                )
            )
        News.objects.bulk_create(cls.news_list)
        cls.news = News.objects.all()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.guest_client = Client()

    def test_bioware_pages_uses_correct_templates(self):
        """Checking that URLs use the appropriate templates."""

        for reverse_name, template in BIOWARE_REVERSE_URL_VS_TEMPLATE.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_index_page_show_correct_context(self):
        """Checking context passed to the index page."""
        response = self.guest_client.get(reverse('bioware:index'))
        self.assertEqual(response.context['game_list'], self.game_list)
        self.assertEqual(response.context['news_list'], self.news_list)
        self.assertTrue(
            response.context['game_list'].object_list[0].image
        )
        self.assertTrue(
            response.context['news_list'].object_list[0].image
        )

    def test_games_page_show_correct_context(self):
        """Checking context passed to the games page."""
        response = self.guest_client.get(reverse('bioware:game_list'))
        self.assertEqual(response.context['game_list'], self.game_list)
        self.assertTrue(
            response.context['game_list'].object_list[0].image
        )
