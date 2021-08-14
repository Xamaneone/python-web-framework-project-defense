import os

from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Review
from tests.base.tests import GamereviewsTestCase


class AddReviewTest(GamereviewsTestCase):
    def test_add_review__when_user_logged_in__expect_added_review(self):
        game, img_path = self.create_game_and_return_game_obj_with_img_path()

        self.client.post(reverse('add review', kwargs={'pk': game.id}), data={
            'text': 'test_text',
            'game_pk': game.id,
        }, follow=True)

        self.assertEqual(Review.objects.first().text, "test_text")
        os.remove(img_path)





