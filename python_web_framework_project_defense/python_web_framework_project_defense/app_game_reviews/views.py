from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from python_web_framework_project_defense.app_game_reviews.forms import ReviewForm
from python_web_framework_project_defense.app_game_reviews.models import Review


def index(request):
    return render(request, 'index.html')


def reviews_list(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews.html', context)


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }

    return render(request, 'reviews/add_review.html', context)


def comment_review(request, pk):
    pass


def about_us(request):
    return render(request, 'abous_us.html')
