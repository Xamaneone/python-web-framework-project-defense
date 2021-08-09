from django.urls import path

from python_web_framework_project_defense.app_game_reviews.views import index, reviews_list, add_review, about_us

urlpatterns = (
    path('', index, name='index'),
    path('reviews/', reviews_list, name='reviews'),
    path('add-review/', add_review, name='add review'),
    path('about-us/', about_us, name='about us'),
)
