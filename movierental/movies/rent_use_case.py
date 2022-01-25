from .models import Movie


class Result:
    pass


class MovieNotFound:
    pass


class MovieRented:
    pass


class MovieAlreadyRented:
    pass


class RentUseCase:

    def invoke(self, movie_uuid):
        movieQuery = Movie.objects.filter(id=movie_uuid)
        if not movieQuery.exists():
            return MovieNotFound()

        movie = movieQuery.first()
        if not movie.available:
            print("llalal")
            return MovieAlreadyRented()

        movie.available = False
        movie.save()
        return MovieRented()
