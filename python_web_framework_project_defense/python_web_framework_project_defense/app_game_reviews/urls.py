from django.urls import path

from python_web_framework_project_defense.app_game_reviews.views import index, reviews_list, add_game_for_review, \
    about_us, game_details, review_game

urlpatterns = (
    path('', index, name='index'),
    path('reviews/', reviews_list, name='reviews'),
    path('add-game/', add_game_for_review, name='add game'),
    path('about-us/', about_us, name='about us'),
    path('reviews/<int:pk>', game_details, name='game details'),
    path('add-review/<int:pk>', review_game, name='add review'),
)
