from .models import Movie


class MovieNotFound:
    pass


class MovieRentSuccess:
    pass


class MovieAlreadyRented:
    pass


class RentUseCase:

    def invoke(self, movie_uuid):
        movie_query = Movie.objects.filter(id=movie_uuid)
        if not movie_query.exists():
            return MovieNotFound()

        movie = movie_query.first()
        if not movie.available:
            return MovieAlreadyRented()

        movie.available = False
        movie.save()
        return MovieRentSuccess()
