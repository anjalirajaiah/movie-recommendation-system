from django.shortcuts import render
from .sentiment import analyze_sentiment
from .models import Movie, Review
from django.db.models import Avg

def home(request):
    result = ""
    recommended_movies = []

    if request.method == "POST":
        review = request.POST.get('review')
        movie_id = request.POST.get('movie')

        movie = Movie.objects.get(id=movie_id)

        # sentiment score
        score = analyze_sentiment(review)

        # save review
        Review.objects.create(
            movie=movie,
            review_text=review,
            sentiment_score=score
        )

        # sentiment result
        if score > 0:
            result = "Positive 😊"
        elif score < 0:
            result = "Negative 😞"
        else:
            result = "Neutral 😐"

    # 🔥 MAIN LOGIC: average sentiment per movie
    movies = Movie.objects.annotate(avg_score=Avg('review__sentiment_score'))

    # filter good movies
    recommended_movies = movies.filter(avg_score__gt=0).order_by('-avg_score')

    # dropdown list
    all_movies = Movie.objects.all()

    return render(request, 'home.html', {
        'result': result,
        'movies': recommended_movies,
        'all_movies': all_movies
    })
