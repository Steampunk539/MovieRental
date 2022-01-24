from django.db import models

# Create your models here.
import uuid
from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class MovieType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    type=models.ForeignKey(MovieType, on_delete=models.CASCADE)
    description=models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.title} {self.author} {self.type}"

