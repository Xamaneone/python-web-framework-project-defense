from django.test import TestCase, Client
from django.urls import reverse


class AboutUsTests(TestCase):
    def test_get_about_us_page(self):
        client = Client()
        response = client.get(reverse('about us'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('abous_us.html')
