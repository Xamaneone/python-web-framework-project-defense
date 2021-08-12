from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
    )
