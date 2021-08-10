from django.contrib import admin

# Register your models here.
from python_web_framework_project_defense.app_game_reviews.models import Game, Review


@admin.register(Game)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    pass
