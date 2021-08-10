from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from python_web_framework_project_defense.app_game_reviews.forms import GameForm, ReviewForm
from python_web_framework_project_defense.app_game_reviews.models import Game, Review
from python_web_framework_project_defense.profiles.models import Profile


def index(request):
    return render(request, 'index.html')


def reviews_list(request):
    reviews = Game.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews.html', context)


@login_required
def add_game_for_review(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect('reviews')
    else:
        form = GameForm()

    context = {
        'form': form,
    }

    return render(request, 'reviews/add_review.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    user = Profile.objects.get(pk=game.user_id)
    review_form = ReviewForm(
        initial={
            'game_pk': pk,
        }
    )

    context = {
        'game': game,
        'uploader': user,
        'reviews': game.review_set.all(),
        'review_form': review_form,
    }

    return render(request, 'game_details.html', context)


@login_required
def review_game(request, pk):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()

    return redirect('game details', pk)


def about_us(request):
    return render(request, 'abous_us.html')
