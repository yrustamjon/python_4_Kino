from django.contrib import admin

from .models import Movie, Actor, Genre, Trailer, Review, View
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)  
admin.site.register(Trailer)
admin.site.register(Review)
admin.site.register(View)  # This line is redundant, you can remove it if you want