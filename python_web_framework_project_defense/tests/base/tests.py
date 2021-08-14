from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client

from python_web_framework_project_defense.app_game_reviews.models import Game

UserModel = get_user_model()


class GamereviewsTestCase(TestCase):
    logged_in_user_name = 'test'
    logged_in_user_password = 'testcase'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username=self.logged_in_user_name,
            password=self.logged_in_user_password,
        )
        self.client.force_login(self.user)

    def create_game_and_return_game_obj_with_img_path(self):
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

        return game, path_to_created_image
