from django.shortcuts import render
from .models import Movie, Author, MovieType
from .serializers import MovieSerializer, AuthorSerializer, MovieTypeSerializer
from rest_framework import generics


# Create your views here.
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieTypeList(generics.ListCreateAPIView):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer


class MovieTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

