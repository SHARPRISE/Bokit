from django.db import models
from artist.models import Artist


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ManyToManyField(Artist)
    year = models.DateTimeField()
    audio = models.FileField()

    def __str__(self):
        return (title + '--' + artist)
