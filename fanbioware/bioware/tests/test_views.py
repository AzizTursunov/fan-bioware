import os
import shutil
import tempfile
from django.urls import reverse
from django.test import Client, TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from fanbioware.utils import BIOWARE_REVERSE_URL_VS_TEMPLATE, NEWS_ON_PAGE, create_test_template
from ..models import Game, News, Opening, Studio

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
                    slug=f'test-game-slug-{i}',
                    description=f'Test game desc #{i}.',
                    image=cls.uploaded,
                    rel_date='2020-02-02',
                    is_released=True
                )
            )
        Game.objects.bulk_create(cls.game_list)
        cls.game_mass_effect = Game.objects.create(
            title='Mass Effect',
            slug='mass-effect',
            description=f'Test game desc.',
            image=cls.uploaded,
            rel_date='2020-02-02',
            is_released=True
        )
        cls.game_list.append(cls.game_mass_effect)
        cls.games = Game.objects.all()
        cls.template_name = create_test_template(
            cls.game_mass_effect.slug
        )
        cls.news_list = []
        for i in range(NEWS_ON_PAGE):
            cls.news_list.append(
                News(
                    game=Game.objects.get(pk=1),
                    title='Test news title for game #1',
                    intro='Test news intro for game #1.',
                    text='Test news text for game #1.',
                    image=cls.uploaded,
                )
            )
        News.objects.bulk_create(cls.news_list)
        cls.news = News.objects.all()

        cls.studio_edmont = Studio.objects.create(
            location='Edmonton, Canada',
            address1='Test studio street',
            address2='Tests studio city',
            zip_code='Test studio zip code',
            phone='Test studio phone',
            email='email@test.com',
            description='Test studio description',
            image=cls.uploaded
        )
        cls.studio_austin = Studio.objects.create(
            location='Austin, US',
            address1='Test studio street',
            address2='Tests studio city',
            zip_code='Test studio zip code',
            phone='Test studio phone',
            email='email@test.com',
            description='Test studio description',
            image=cls.uploaded
        )

        cls.opening_edmont = Opening.objects.create(
            studio=cls.studio_edmont,
            team='Test team 1',
            role='Test role 1',
            description='Test desc of the studio',
            remote=True,
            responsibilities='First_test_resp;Second_test_resp',
            qualifications='First_test_qualif;Second_test_qualif',
            perks='First_test_perk;Second_test_perk'
        )
        cls.opening_austin = Opening.objects.create(
            studio=cls.studio_austin,
            team='Test team 2',
            role='Test role 2',
            description='Test desc of the studio',
            remote=True,
            responsibilities='First_test_resp;Second_test_resp',
            qualifications='First_test_qualif;Second_test_qualif',
            perks='First_test_perk;Second_test_perk'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        os.remove(cls.template_name)

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
        response_game_list = response.context['game_list']
        self.assertEqual(
            list(response_game_list),
            self.game_list
        )
        self.assertEqual(
            response_game_list.first().title,
            self.games.first().title
        )
        self.assertEqual(
            response_game_list.first().news.first().title,
            self.news.first().title
        )
        self.assertTrue(response_game_list.first().image)
        self.assertTrue(response_game_list.first().news.first().image)

    def test_games_page_show_correct_context(self):
        """Checking context passed to the games page."""
        response = self.guest_client.get(reverse('bioware:game_list'))
        self.assertEqual(
            list(response.context['game_list']),
            self.game_list
        )
        first_game = response.context['game_list'].first()
        self.assertTrue(first_game.image)
        self.assertEqual(first_game.title, self.games.first().title)
        self.assertEqual(
            first_game.description,
            self.games.first().description
        )
        self.assertEqual(first_game.platforms, self.games.first().platforms)

    def test_contacts_page_show_correct_context(self):
        """Checking context passed to the contacts page."""
        response = self.guest_client.get(reverse('bioware:contacts'))
        studio_austin = response.context['studio_list'].get(
            location='Austin, US'
        )
        self.assertEqual(studio_austin.address1, self.studio_austin.address1)
        self.assertEqual(studio_austin.phone, self.studio_austin.phone)
        self.assertEqual(studio_austin.zip_code, self.studio_austin.zip_code)
        self.assertTrue(studio_austin.image)

    def test_careers_page_show_correct_context(self):
        """Checking context passed to the careers page."""
        response = self.guest_client.get(reverse('bioware:careers'))
        studio = response.context['opening_list'].first()
        self.assertIn(studio, (self.opening_edmont, self.opening_austin))
