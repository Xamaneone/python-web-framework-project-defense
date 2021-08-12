from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Game, UserModel, Review
from tests.base.tests import GamereviewsTestCase


class GameDetailsTest(GamereviewsTestCase):
    def test_GameDetails__when_game_exist_and_is_owner__expect_to_return_details(self):
        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=self.user,
        )

        response = self.client.get(reverse('game details', kwargs={'pk': game.id, }))

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['game'].user.id, self.user.id)

    def test_GameDetails__when_game_exist_and_is_not_owner__expect_to_return_details(self):
        test_user = UserModel.objects.create_user(
            username='test_name',
            password='test_password',
        )

        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=test_user,
        )

        response = self.client.get(reverse('game details', kwargs={'pk': game.id, }))

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(response.context['game'].user.id, self.user.id)

    def test_game_Details__when_game_exist_without_review__expect__to_return_reviews(self):
        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=self.user,
        )

        response = self.client.get(reverse('game details', kwargs={'pk': game.id, }))

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(list(response.context['reviews']))

    def test_game_Details__when_game_exist_with_review__expect_review(self):
        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=self.user,
        )
        review = Review.objects.create(
            text='Test',
            game=game,
            user=self.user,
        )

        response = self.client.get(reverse('game details', kwargs={'pk': game.id, }))

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['reviews'][0].user.id, review.user.id)
        self.assertListEqual([review], list(response.context['reviews']))
