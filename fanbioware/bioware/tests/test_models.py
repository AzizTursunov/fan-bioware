import shutil
import tempfile
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from fanbioware.utils import (TestHelpTextMixin, TestVerboseNameMixin,
                              TestFiedlMaxLengthMixin)
from ..models import Game, News, Opening, Studio

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ModelFixtures(TestCase):
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
            title='Test title',
            slug='test-game',
            description='Test desc',
            image=cls.uploaded,
            rel_date='2020-10-15'
        )
        cls.news = News.objects.create(
            game=cls.game,
            title='Test news title',
            intro='Test news intro',
            text='Test news text',
            image=cls.uploaded
        )
        cls.studio = Studio.objects.create(
            location='Test studio City, Test studio Country',
            address1='Test studio street',
            address2='Tests studio city',
            zip_code='Test studio zip code',
            phone='Test studio phone',
            email='email@test.com',
            description='Test studio description',
            image=cls.uploaded
        )
        cls.opening = Opening.objects.create(
            studio=cls.studio,
            team='Test openings team',
            role='Test openings role',
            description='Test openings desc'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)


class GameModelTest(ModelFixtures, TestHelpTextMixin,
                    TestVerboseNameMixin, TestFiedlMaxLengthMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_and_verbose_name = {
            'title': 'Name of the game',
            'description': 'Description',
            'image': 'Cover',
            'platforms': 'Platforms',
            'rel_date': 'Release date',
            'genre': 'Genre'
        }

        cls.field_and_help_text = {
            'title': 'Enter the name of the game',
            'description': 'Enter a description of the game',
            'image': 'Attach the cover of the game',
            'platforms': 'Select the available platforms',
            'rel_date': 'Enter the release date',
            'genre': 'Select the game genre'
        }

        cls.field_and_max_len = {
            'intro': 650
        }

    def test_game_str_method(self):
        """Checking the method __str__ of the Game model."""
        self.assertEqual(str(self.game), self.game.title)

    def test_game_model_fields_verbose_name(self):
        """Checking fields verbose_name of the Game model."""
        super().run_verbose_name_test(self.game)

    def test_game_model_fields_help_text(self):
        """Checking fields help_text of the Game model."""
        super().run_help_text_test(self.game)

    def test_game_model_fields_max_length(self):
        """Checking maximum length of the Game model fields."""
        super().run_fields_max_len_test(self.game)


class NewsModelTest(ModelFixtures, TestHelpTextMixin,
                    TestVerboseNameMixin, TestFiedlMaxLengthMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_and_verbose_name = {
            'game': 'Game',
            'title': 'Title',
            'intro': 'Intro',
            'text': 'Text',
            'image': 'Cover',
        }

        cls.field_and_help_text = {
            'game': 'Choose the game',
            'title': 'Enter a title of the news',
            'intro': 'Enter a short intro of the news',
            'text': 'Enter the news text',
            'image': 'Attach the cover of the news',
        }

        cls.field_and_max_len = {
            'title': 45,
            'intro': 90
        }

    def test_news_str_method(self):
        """Checking the method __str__ of the News model."""
        self.assertEqual(str(self.news), self.news.title)

    def test_news_model_fields_verbose_name(self):
        """Checking fields verbose_name of the News model."""
        super().run_verbose_name_test(self.news)

    def test_news_model_fields_help_text(self):
        """Checking fields help_text of the News model."""
        super().run_help_text_test(self.news)

    def test_news_model_fields_max_length(self):
        """Checking maximum length of the News model fields."""
        super().run_fields_max_len_test(self.news)


class OpeningModelTest(ModelFixtures, TestHelpTextMixin,
                       TestVerboseNameMixin, TestFiedlMaxLengthMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_and_verbose_name = {
            'studio': 'Studio',
            'team': 'Team',
            'role': 'Role',
            'description': 'Description',
            'emp_type': 'Type of employment',
            'remote': 'Remote',
            'responsibilities': 'Responsibilities',
            'qualifications': 'Qualifications',
            'perks': 'Perks'
        }

        cls.field_and_help_text = {
            'studio': 'Choose the studio',
            'team': 'Enter the team',
            'role': 'Enter the role',
            'description': 'Enter a description of the opening',
            'emp_type': 'Choose the type of employment',
            'remote': 'Remote is accessible',
            'responsibilities': (
                'Describe the responsibilities '
                'separated by semicolons'
            ),
            'qualifications': (
                'Describe the responsibilities separated by semicolons'
            ),
            'perks': 'Describe the perks separated by semicolons'
        }

    def test_opening_str_method(self):
        """Checking the method __str__ of the Opening model."""
        self.assertEqual(str(self.opening), self.opening.role)

    def test_opening_model_fields_verbose_name(self):
        """Checking fields verbose_name of the Opening model."""
        super().run_verbose_name_test(self.opening)

    def test_opening_model_fields_help_text(self):
        """Checking fields help_text of the Opening model."""
        super().run_help_text_test(self.opening)


class StudioModelTest(ModelFixtures, TestHelpTextMixin,
                      TestVerboseNameMixin, TestFiedlMaxLengthMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_and_verbose_name = {
            'location': 'Location',
            'address1': 'Address',
            'address2': 'City',
            'zip_code': 'Zip Code',
            'phone': 'Phone',
            'email': 'Email',
            'description': 'Description',
            'image': 'Cover',
        }
        cls.field_and_help_text = {
            'location': (
                'Enter the name of the city and '
                'country separated by commas'
            ),
            'address1': 'Enter the street name and building number',
            'address2': 'Enter the city',
            'zip_code': 'Enter the zip code',
            'phone': 'Enter the phone number',
            'email': 'Enter e-mail',
            'description': 'Enter a description of the studio',
            'image': 'Attach the cover of the studio',
        }

    def test_studio_str_method(self):
        """Checking the method __str__ of the Studio model."""
        self.assertEqual(str(self.studio), self.studio.location)

    def test_studio_model_fields_verbose_name(self):
        """Checking fields verbose_name of the Studio model."""
        super().run_verbose_name_test(self.studio)

    def test_studio_model_fields_help_text(self):
        """Checking fields help_text of the Studio model."""
        super().run_help_text_test(self.studio)
