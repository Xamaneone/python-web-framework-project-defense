from django import forms

from python_web_framework_project_defense.app_game_reviews.models import Game, Review


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('user',)


class ReviewForm(forms.ModelForm):
    game_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Review
        exclude = ('user', 'game',)

    def save(self, commit=True):
        game_pk = self.cleaned_data['game_pk']
        game = Game.objects.get(pk=game_pk)
        review = Review(
            text=self.cleaned_data['text'],
            game=game
        )

        if commit:
            review.save()

        return review
