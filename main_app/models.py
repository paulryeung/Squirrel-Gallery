from django.db import models
from django.urls import reverse

# Create your models here.
class Squirrel(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    country_found = models.CharField(max_length=100, verbose_name='Countries Found')
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'sq_id': self.id })