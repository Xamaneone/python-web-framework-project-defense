import random
import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import join
from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Game
from tests.base.tests import GamereviewsTestCase


class AddGameTest(GamereviewsTestCase):
    def test_add_game__when_not_user_logged_in__expect_redirect(self):
        self.client.logout()

        response = self.client.get(reverse('add game'))

        self.assertEqual(302, response.status_code)

    def test_add_game_get_method__when_user_logged__expect_form(self):
        response = self.client.get(reverse('add game'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'reviews/add_game.html')

    def test_add_game_with_no_data__when_user_logged__except_no_added_game(self):
        response = self.client.post(reverse('add game'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(Game.objects.all().count(), 0)

    # def test_add_game_post_method__when_user_logged__expect_to_(self):
    #     path_to_image = f"{settings.BASE_DIR}/tests/media/test_image.png"  # not working
    #     path_to_created_image = f"{settings.BASE_DIR}/media/game_photos/test_image.png"
    #
    #     file_name = f'test_image.png'
    #     file = SimpleUploadedFile(
    #         name=file_name,
    #         content=open(path_to_image, 'rb').read(),
    #         content_type='image/png',
    #     )
    #
    #     response = self.client.post(reverse('add game'), data={
    #         'title': 'title',
    #         'description': 'description',
    #         'image': file,
    #         'user': self.user,
    #     }, follow=True)
    #
    #     self.assertEqual(Game.objects.first().title, 'title')
    #     os.remove(path_to_created_image)
