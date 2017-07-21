from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    mediums = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

class Medium(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
