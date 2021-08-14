import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Game
from tests.base.tests import GamereviewsTestCase


class DeleteGameTest(GamereviewsTestCase):
    def test_delete_game_post__when_user_logged__except_game_to_be_deleted(self):
        path_to_image = f"{settings.BASE_DIR}/tests/media/test_image.png"
        path_to_created_image = f"{settings.BASE_DIR}/media/game_photos/test_image.png"

        file_name = f'test_image.png'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/png',
        )

        game = Game.objects.create(
            title='title',
            description='description',
            image=file,
            user=self.user,
        )

        response = self.client.post(reverse('delete game', kwargs={'pk': game.id, }))

        self.assertEqual(302, response.status_code)
        self.assertTemplateUsed('reviews.html')

        os.remove(path_to_created_image)


    def test_delete_game_get__when_user_logged__except_template(self):
        path_to_image = f"{settings.BASE_DIR}/tests/media/test_image.png"
        path_to_created_image = f"{settings.BASE_DIR}/media/game_photos/test_image.png"

        file_name = f'test_image.png'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/png',
        )

        game = Game.objects.create(
            title='title',
            description='description',
            image=file,
            user=self.user,
        )

        response = self.client.get(reverse('delete game', kwargs={'pk': game.id, }))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed('delete_game.html')

        os.remove(path_to_created_image)
