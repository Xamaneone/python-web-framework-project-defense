from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Review(models.Model):
    title = models.CharField(
        max_length=40,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='game_photos',
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    text = models.TextField()
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

###TODO COMPLETE ME
