from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Author, MovieType
from .rent_use_case import RentUseCase, MovieNotFound, MovieAlreadyRented
from .serializers import MovieSerializer, AuthorSerializer, MovieTypeSerializer
from rest_framework import generics, status


# Create your views here.
class RentMovie(APIView):

    rentUseCase = RentUseCase

    def put(self, request, pk):
        result = self.rentUseCase().invoke(pk)
        print(type(result))
        status_code = status.HTTP_202_ACCEPTED
        status_message = "Movie Rented"
        if isinstance(result, MovieNotFound):
            status_code = status.HTTP_404_NOT_FOUND
            status_message = "Movie not found"
        if isinstance(result, MovieAlreadyRented):
            status_code = status.HTTP_208_ALREADY_REPORTED
            status_message = "Movie already rented"
        return Response(
            status=status_code,
            data={
                "status": status_message
            }
        )


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

