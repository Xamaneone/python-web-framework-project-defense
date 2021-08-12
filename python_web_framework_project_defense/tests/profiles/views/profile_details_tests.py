from django.contrib.auth import get_user_model
from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Game
from tests.base.tests import GamereviewsTestCase

UserModel = get_user_model()


class ProfileDetailsTest(GamereviewsTestCase):
    def test__get_details_own_profile__when_logged_in_user__except_details_with_no_games(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile', args=[self.user.id]))

        games = list(response.context['games'])
        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(games)
        self.assertEqual(self.user.id, profile.user_id)

    def test__get_details_own_profile__when_logged_in_user_with_games__except_details_with_games(self):
        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=self.user,
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile', args=[self.user.id]))

        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, profile.user_id)
        self.assertListEqual([game], list(response.context['games']))

    def test__get_details_another_profile__when_logged_in_user__except_details_with_no_games(self):
        self.client.force_login(self.user)
        TestUser = UserModel.objects.create_user(username='TestUser', password='testcase')
        response = self.client.get(reverse('profile', args=[TestUser.id]))

        games = list(response.context['games'])
        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(games)
        self.assertEqual(TestUser.id, profile.user_id)
        self.assertNotEqual(self.user.id, profile.user_id)

    def test__get_details_another_profile__when_logged_in_user_with_games__except_details_with_games(self):
        TestUser = UserModel.objects.create_user(username='TestUser', password='testcase')
        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=TestUser,
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile', args=[TestUser.id]))

        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertEqual(TestUser.id, profile.user_id)
        self.assertListEqual([game], list(response.context['games']))

    def test__get_details_profile__when_not_logged_in_user__except_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('profile', args=[self.user.id]))

        self.assertEqual(302, response.status_code)
