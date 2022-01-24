from django.contrib import admin
from .models import Movie, Author, MovieType

# Register your models here.
admin.site.register(Movie)
admin.site.register(Author)
admin.site.register(MovieType)
