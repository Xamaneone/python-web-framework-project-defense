from django.contrib.auth import get_user_model
from django.test import TestCase, Client

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
