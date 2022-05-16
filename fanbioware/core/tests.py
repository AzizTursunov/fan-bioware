from http import HTTPStatus
from django.test import TestCase


class CoreViewTest(TestCase):
    def test_unexisting_url_not_exists(self):
        """Check that request to /unexisting-page/ return 404 error and
        template core/errors.html will be used.
        """
        response = self.client.get('/unexisting-page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertTemplateUsed(response, 'core/errors.html')
