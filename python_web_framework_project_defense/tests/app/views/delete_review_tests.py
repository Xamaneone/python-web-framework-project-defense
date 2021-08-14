import os

from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Review
from tests.base.tests import GamereviewsTestCase


class DeleteReviewTest(GamereviewsTestCase):
    def test_edit_review__when_user_logged_in__expect_review_edited(self):
        game, img_path = self.create_game_and_return_game_obj_with_img_path()

        review = Review.objects.create(
            text='text',
            user=self.user,
            game=game
        )

        self.client.post(reverse('delete review', kwargs={'pk': game.id}))

        self.assertListEmpty(list(Review.objects.all()))
        os.remove(img_path)

