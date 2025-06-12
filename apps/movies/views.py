from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Movie,Genre,Review,View
from django.db.models import Avg

def movies_view(request,):
    search= request.GET.get('search')
    genre= request.GET.get('genre')
    
    movies = Movie.objects.all()
    
    if genre:
        movies = movies.filter(genres__name=genre)
    if search:
        movies = movies.filter(title__icontains=search)
    return render(request, 'movies.html', {'movies': movies, 'Genres': Genre.objects.all(), 'selected_genre': genre})

def movie_view(request, pk):
    movie = Movie.objects.get(id=pk)
    if not View.objects.filter(movie=movie, address=request.META.get('REMOTE_ADDR')).exists():
        View.objects.create(movie=movie, address=request.META.get('REMOTE_ADDR'))
    rating_data = Review.objects.filter(movie=movie).aggregate(Avg('rating'))
    avg_rating = rating_data['rating__avg']
    if avg_rating:
        avg_rating = round(avg_rating, 1)  # 1 kasr belgisi
    return render(request, 'movie.html', context={
        'movie': movie,
        'rating': avg_rating,
        'reviews': movie.review_set.all(),
        'view': movie.view_set.all().count(),
    })


def add_review_view(request,pk):
    comment = request.POST.get('comment')
    rating= request.POST.get('rating')
    name=request.POST.get('name')
    email=request.POST.get('email')
    movie=Movie.objects.get(id=pk)
    
    Review.objects.create(
        name=name,
        email=email,
        comment=comment,
        rating=rating,
        movie=movie,
    )
    return redirect(reverse('movie', kwargs={'pk': pk}))