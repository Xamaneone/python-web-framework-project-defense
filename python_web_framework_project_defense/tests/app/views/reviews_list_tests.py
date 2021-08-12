from django.contrib.auth import get_user_model
from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Game
from tests.base.tests import GamereviewsTestCase


class GameListTests(GamereviewsTestCase):
    def test__list_games_when_empty__expect_empty_list(self):
        response = self.client.get(reverse('reviews'))

        reviews = list(response.context['reviews'])

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(reviews)

    def test__list_games_when_not_empty__expect_list(self):
        game = Game.objects.create(
            title='Test Game',
            description='Test game description',
            image='path_to_image.png',
            user=self.user,
        )

        response = self.client.get(reverse('reviews'))

        reviews = list(response.context['reviews'])

        self.assertEqual(200, response.status_code)
        self.assertListEqual([game], reviews)

