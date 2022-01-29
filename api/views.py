from django.shortcuts import render
from api.models import Movie, Genre
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView

from .serializer import MovieSerializer, GenreSerializer
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

# SHOW MOVIES
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination #pagination
    filter_backend = [DjangoFilterBackend,] #filter list
    filterset_fields = ['title', 'genre__name', 'language', 'type'] #genre was a foreign key to Movie so we move into Genre and then filter

# ADD MOVIE
class MovieCreateView(CreateAPIView):
    serializer_class = MovieSerializer 

# MOVIE DETAIL VIEW
class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    lookup_field = 'title'
    serializer_class = MovieSerializer

# MOVIE GENRE
class GenreCreateListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backend = [DjangoFilterBackend,] #filter list
    filterset_fields = ['name',]