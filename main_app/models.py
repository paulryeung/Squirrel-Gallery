from django.db import models
from django.urls import reverse

from datetime import date


#choices in form of nested tuples
ACTIVITY= (
    ('R', 'Ran around'),
    ('C', 'Climbed trees'),
    ('S', 'Stole from the garden')
)

class Food(models.Model):
    name = models.CharField(max_length=50)
    foodtype = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'pk': self.id})

# Create your models here.
class Squirrel(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    country_found = models.CharField(max_length=100, verbose_name='Countries Found')
    age = models.IntegerField()

    food = models.ManyToManyField(Food)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'sq_id': self.id })

    def no_visits_today(self):
        return self.visit_set.filter(date=date.today()).count() > 0
        

class Visit(models.Model):
    date = models.DateField()
    activity = models.CharField(max_length=1, choices=ACTIVITY, default=ACTIVITY[0][0])
    squirrel = models.ForeignKey(Squirrel, on_delete=models.CASCADE)

    def __str__ (self):
        return f'{self.get_activity_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

    
