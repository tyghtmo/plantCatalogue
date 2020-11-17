from django.db import models
from django.urls import reverse


# TODO Plant model not actually used yet. Does it need to be?
class Plant(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    id = models.CharField(max_length=255, primary_key=True)

    class Meta:
        ordering = ['-slug']

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('plant', args=[self.slug])

# TODO Implement User model that can save favourite plants
