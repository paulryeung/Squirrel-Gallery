from django.shortcuts import render
from django.http import HttpResponse

#For now put models here
class Squirrel:
    def __init__(self, name, species, description, country_found, age):
        self.name = name
        self.species = species
        self.description = description
        self.country_found = country_found
        self.age = age

squirrels = [
    Squirrel('Bob', "Eastern Gray", "gray and bushy", "Canada", 2),
    Squirrel('Nick', "American Red", "red and fury", "United States", 0),
    Squirrel('Jumpy', "Northern Flying", "jumps and glides", "Canada, United States", 4)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Squirrel Gallery! </h1>')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'squirrels/index.html', {'squirrels': squirrels})