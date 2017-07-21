from django.db import models
from pictures.models import ERAS

# Create your models here.
ERAS = (
    ('1', '1950'),
    ('2', '1960'),
    ('3', '1970'),
    ('4', '1980'),
    ('5', '1990'),
    ('6', '2000'),
    ('7', '2010'),
    ('99', 'Unknown')
)


class Literature(models.Model):
    title = models.CharField(max_length=100, default='Text Title')
    author = models.CharField(max_length=50, default='Author')
    description = models.CharField(max_length=150, default='Description')
    cover_picture = models.ImageField('img', upload_to='media/', blank=True)
    era = models.CharField(max_length=255, choices=ERAS, default='Unknown')
    date_posted = models.DateField(auto_now_add=True, verbose_name='Posted on')
    poster = models.CharField(max_length=255, default='Poster')
    slug = models.SlugField(unique=True, max_length=255, default='slug')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('literature.views.text', args=[self.slug])
