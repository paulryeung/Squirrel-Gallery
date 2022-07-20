from django.shortcuts import render
# from django.http import HttpResponse
from . models import Squirrel
from django.views.generic.edit import CreateView, DeleteView, UpdateView

#For now put models here
# class Squirrel:
#     def __init__(self, name, species, description, country_found, age):
#         self.name = name
#         self.species = species
#         self.description = description
#         self.country_found = country_found
#         self.age = age

# squirrels = [
#     Squirrel('Bob', "Eastern Gray", "gray and bushy", "Canada", 2),
#     Squirrel('Nick', "American Red", "red and fury", "United States", 0),
#     Squirrel('Jumpy', "Northern Flying", "jumps and glides", "Canada, United States", 4)
# ]



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'squirrels/index.html', {'squirrels': squirrels})

def squirrel_details(request, sq_id):
    squirrel = Squirrel.objects.get(id = sq_id)
    return render(request, 'squirrels/detail.html', {'squirrel': squirrel})

class SqCreate(CreateView):
    model = Squirrel
    fields = '__all__'

class SqDelete(DeleteView):
    model = Squirrel
    success_url = '/squirrels/'

class SqUpdate(UpdateView):
    model = Squirrel
    fields = ['species', 'description', 'country_found', 'age']