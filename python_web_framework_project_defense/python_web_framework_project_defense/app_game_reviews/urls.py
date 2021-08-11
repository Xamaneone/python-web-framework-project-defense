from django.urls import path

from python_web_framework_project_defense.app_game_reviews.views import index, reviews_list, add_game_for_review, \
    about_us, game_details, review_game, delete_review, edit_review, delete_game, edit_game

urlpatterns = (
    path('', index, name='index'),
    path('reviews/', reviews_list, name='reviews'),
    path('add-game/', add_game_for_review, name='add game'),
    path('edit-game/<int:pk>', edit_game, name='edit game'),
    path('delete-game/<int:pk>', delete_game, name='delete game'),
    path('about-us/', about_us, name='about us'),
    path('reviews/<int:pk>', game_details, name='game details'),
    path('add-review/<int:pk>', review_game, name='add review'),
    path('edit-review/<int:pk>', edit_review, name='edit review'),
    path('delete-review/<int:pk>', delete_review, name='delete review'),
)
