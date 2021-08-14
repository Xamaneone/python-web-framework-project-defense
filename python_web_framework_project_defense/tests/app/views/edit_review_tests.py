import os

from django.urls import reverse

from python_web_framework_project_defense.app_game_reviews.models import Review
from tests.base.tests import GamereviewsTestCase


class EditReviewTest(GamereviewsTestCase):
    def test_edit_review__when_user_logged_in__expect_review_edited(self):
        game, img_path = self.create_game_and_return_game_obj_with_img_path()

        review = Review.objects.create(
            text='text',
            user=self.user,
            game=game
        )

        self.client.post(reverse('edit review', kwargs={'pk': game.id}), data={
            'text': 'test_text',
        }, follow=True)

        self.assertEqual(Review.objects.first().text, "test_text")
        os.remove(img_path)

    def test_edit_review_get__when_user_logged_in__expect_template(self):
        game, img_path = self.create_game_and_return_game_obj_with_img_path()

        review = Review.objects.create(
            text='text',
            user=self.user,
            game=game
        )

        self.client.get(reverse('edit review', kwargs={'pk': review.id}))

        self.assertTemplateUsed('edit_review.html')
        os.remove(img_path)

