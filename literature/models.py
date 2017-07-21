from django.db import models
from pictures.models import ERAS

# Create your models here.

class Literature(models.Model):
    title = models.CharField(max_length=100, default='Text Title')
    author = models.CharField(max_length=50, default='Author')
    description = models.CharField(max_length=150, default='Description')
    cover_picture = models.ImageField('img', upload_to='media/', blank=True)
    era = models.CharField(max_length=255, choices=ERAS, default='Unknown')
    date_posted = models.DateField(auto_now_add=True, verbose_name='Posted on')
    poster = models.CharField(max_length=255, default='Poster')
    slug = models.SlugField(unique=True, max_length=255, default='slug')
