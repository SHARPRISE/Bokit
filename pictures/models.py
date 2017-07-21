from django.db import models

# Create your models here.

ERAS = (
    ('1', 'Pre-Colonial/Tainos'),
    ('2', 'Colonial'),
    ('3', 'Independance War'),
    ('4', '19th Century'),
    ('5', '20th Century'),
    ('6', '21st Century/Modern')
)

class PictureArt(models.Model):
    title = models.CharField(max_length=100, default='Art Title')
    creator = models.CharField(max_length=50, default='Creator')
    description = models.CharField(max_length=150, default='Art description')
    art_picture = models.ImageField('img', upload_to='media/', blank=False)
    era = models.CharField(max_length=255, choices=ERAS, default='Unknown')
    date_posted = models.DateField(auto_now_add=True, verbose_name='Posted on')
    poster = models.CharField(max_length=255, default='Poster')
    slug = models.SlugField(unique=True, max_length=255, default='slug')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

#    def get_absolute_url(self):
#        return reverse('pictures.views.picture', args=[self.slug])
