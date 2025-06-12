from django.urls import path
from .views import movies_view, movie_view,add_review_view

urlpatterns = [
    path('',movies_view, name='movies'),
    path('<int:pk>/',movie_view,name='movie'),
    path('add-review/<int:pk>', add_review_view, name='add_review'),
]
