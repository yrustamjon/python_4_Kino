from django.db import models

from apps.common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Actor(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_in = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='actors', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField()
    duration = models.DurationField()
    poster = models.ImageField(upload_to='movies/poster', blank=True, null=True)
    cast = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    video=models.FileField(upload_to="movies/movie_files", blank=True, null=True)

    def __str__(self):
        return self.title


class Trailer(BaseModel):
    title = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    youtube_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.movie.title}"


class Review(BaseModel):
    rating = models.SmallIntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_set')
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.movie} - {self.rating}"

class View(BaseModel):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='view_set', blank=True, null=True)  
    address=models.GenericIPAddressField(blank=True, null=True)
    def __str__(self):
        return f"{self.movie} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    