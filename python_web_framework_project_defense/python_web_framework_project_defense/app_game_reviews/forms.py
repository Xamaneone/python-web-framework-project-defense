from django import forms

from python_web_framework_project_defense.app_game_reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', )
