from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class SignInForm(forms.Form):
    user = None
    username = forms.CharField(
        max_length=150,
    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(),
    )

    def clean(self):
        # On clean, check if the user exist
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            # If the user doesn't exist, raise validation error
            raise ValidationError('Username or password incorrect')

    def save(self):
        # Return the user
        return self.user


