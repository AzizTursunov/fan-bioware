from django.test import TestCase
from fanbioware.utils import (TestHelpTextMixin, TestVerboseNameMixin,
                              TestFiedlMaxLengthMixin)
from ..models import Game, News, Opening, Studio


class ModelFixtures(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.game = Game.objects.create()
        cls.news = News.objects.create()
        cls.opening = Opening.objects.create()
        cls.studio = Studio.objects.create()


class GameModelTest(ModelFixtures, TestHelpTextMixin,
                    TestVerboseNameMixin, TestFiedlMaxLengthMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.field_and_verbose_name = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Cover',
            'platforms': 'Platforms',
            'release_date': 'Release date',
            'genre': 'Genre'
        }

        cls.field_and_help_text = {
            'title': 'Enter the name of the game',
            'description': 'Enter a description of the game',
            'image': 'Attach the cover of the game',
            'platforms': 'Select the available platforms',
            'release_date': 'Enter the release date',
            'genre': 'Select the game genre'
        }

        cls.field_and_max_len = {
            'description': 650
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
            'tags': 'Tags'
        }

        cls.field_and_help_text = {
            'game': 'Choose the game',
            'title': 'Enter a title of the news',
            'intro': 'Enter a short intro of the news',
            'text': 'Enter the news text',
            'image': 'Attach the cover of the news',
            'tags': 'Add the news tags'
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
            'dsecription': 'Description',
            'remote': 'Remote',
            'responsibilities': 'Responsibilities',
            'qualifications': 'Qualifications',
            'perks': 'Perks'
        }

        cls.field_and_help_text = {
            'studio': 'Choose the studio',
            'team': 'Enter the team',
            'role': 'Enter the role',
            'dsecription': 'Enter a description of the opening',
            'remote': 'Choose the type of employment',
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
            'mail': 'Email',
            'description': 'Description',
            'image': 'Cover',
            'openings': 'Openings'
        }
        cls.field_and_verbose_name = {
            'location': (
                'Enter the name of the city and '
                'country separated by commas'
            ),
            'address1': 'Enter the street name and building number',
            'address2': 'Enter the city',
            'zip_code': 'Enter the zip code',
            'phone': 'Enter the phone number',
            'mail': 'Enter e-mail',
            'description': 'Enter a description of the studio',
            'image': 'Attach the cover of the news',
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
