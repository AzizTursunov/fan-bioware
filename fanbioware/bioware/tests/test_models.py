from django.test import TestCase
from fanbioware.utils import (TestHelpTextMixin, TestVerboseNameMixin,
                              TestFiedlMaxLengthMixin)
from ..models import Games, News, Openings


class ModelFixtures(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.game = Games.objects.create()
        cls.news = News.objects.create()
        cls.openings = Openings.objects.create()


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

    def test_games_str_method(self):
        """Checking the method __str__ of the Games model."""
        self.assertEqual(str(self.game), self.game.title)

    def test_games_model_fields_verbose_name(self):
        """Checking fields verbose_name of the Games model."""
        super().run_verbose_name_test(self.game)

    def test_games_model_fields_help_text(self):
        """Checking fields help_text of the Games model."""
        super().run_help_text_test(self.game)

    def test_games_model_fields_max_length(self):
        """Checking maximum length of the Games model fields."""
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
