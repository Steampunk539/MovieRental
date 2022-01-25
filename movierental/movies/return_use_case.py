from .models import Movie


class MovieNotFound:
    pass


class MovieReturnSuccess:
    pass


class MovieNotRented:
    pass


class ReturnUseCase:

    def invoke(self, movie_uuid):
        movie_query = Movie.objects.filter(id=movie_uuid)
        if not movie_query.exists():
            return MovieNotFound()

        movie = movie_query.first()
        if not movie.available:
            print("Udało się zwrócić")
            movie.available = True
            movie.save()
            return MovieReturnSuccess()

        print("Film nie był wypożyczony")
        return MovieNotRented()
