import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Game
from tests.base.tests import GamereviewsTestCase


class EditGameTest(GamereviewsTestCase):
    def test_edit_get__when_user_not_logged__except_redirect(self):
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
        self.client.logout()

        response = self.client.post(reverse('edit game', kwargs={'pk': game.id, }), data={
            'title': 'test_title',
            'description': 'test_description',
            'image': file,
            'user': self.user,
        }, follow=True)

        self.assertTemplateUsed('auth/login.html')
        os.remove(path_to_created_image)

    def test_edit_game_post_method__when_user_logged__expect_to_add_game(self):
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

        self.client.post(reverse('edit game', kwargs={'pk': game.id, }), data={
            'title': 'test_title',
            'description': 'test_description',
            'image': file,
            'user': self.user,
        }, follow=True)

        self.assertEqual(Game.objects.first().title, 'test_title')
        self.assertEqual(Game.objects.first().description, 'test_description')
        os.remove(path_to_created_image)


    def test_edit_game_get_method__when_user_logged__expect_specific_template(self):
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

        self.client.get(reverse('edit game', kwargs={'pk': game.id, }))

        self.assertTemplateUsed('edit_game.html')
        os.remove(path_to_created_image)

