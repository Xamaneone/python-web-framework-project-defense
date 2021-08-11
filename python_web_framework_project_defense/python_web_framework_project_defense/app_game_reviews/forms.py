from django import forms

from python_web_framework_project_defense.app_game_reviews.models import Game, Review


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('user',)


class ReviewForm(forms.ModelForm):
    game_pk = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False,
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


class EditReviewForm(ReviewForm):
    class Meta:
        model = Review
        exclude = ('user', 'game', 'game_pk')

    def save(self, commit=True):
        """
        Save this form's self.instance object if commit=True. Otherwise, add
        a save_m2m() method to the form which can be called after the instance
        is saved manually at a later time. Return the model instance.
        """
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate." % (
                    self.instance._meta.object_name,
                    'created' if self.instance._state.adding else 'changed',
                )
            )
        if commit:
            # If committing, save the instance and the m2m data immediately.
            self.instance.save()
            self._save_m2m()
        else:
            # If not committing, add a method to the form to allow deferred
            # saving of m2m data.
            self.save_m2m = self._save_m2m
        return self.instance


