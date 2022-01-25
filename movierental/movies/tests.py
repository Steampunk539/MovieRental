from django.test import TestCase
from .models import Movie, MovieType, Author

# Create your tests here.
from .rent_use_case import *


class BaseTestClass(TestCase):

    def setUp(self):
        self.mock_type = MovieType.objects.create(name="test", description="test")
        self.mock_author = Author.objects.create(name="Test", surname="Test")
        self.mock_movie = Movie.objects.create(title="TestMovie", author=self.mock_author, type=self.mock_type)
        self.mock_rented_movie = Movie.objects.create(title="TestMovie", author=self.mock_author, type=self.mock_type, available=False)

    def test_movie_with_correct_id_returns_movie_rent_success(self):
        result = RentUseCase().invoke(self.mock_movie.id)
        self.assertIsInstance(result, MovieRentSuccess)

    def test_movie_with_wrong_id_returns_movie_not_found(self):
        result = RentUseCase().invoke("123e4567-e89b-12d3-a456-426614174000")
        self.assertIsInstance(result, MovieNotFound)

    def test_movie_with_correct_id_already_rented_returns_movie_already_rented(self):
        result = RentUseCase().invoke(self.mock_rented_movie.id)
        self.assertIsInstance(result, MovieAlreadyRented)
