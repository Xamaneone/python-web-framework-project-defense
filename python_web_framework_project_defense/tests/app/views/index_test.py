from django.urls import reverse

from tests.base.tests import GamereviewsTestCase


class IndexTest(GamereviewsTestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')
