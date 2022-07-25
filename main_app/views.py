from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Squirrel, Food
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import VisitForm

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
    visit_form = VisitForm()

    #query finding all food treats squirrel doesn't have
    treats_squirrel_doesnt_have = Food.objects.exclude(id__in = squirrel.food.all().values_list('id'))

    #show visits form and treats squirrel doesn't have
    return render(request, 'squirrels/detail.html', {
        'squirrel': squirrel, 'visit_form': visit_form,
        'treats': treats_squirrel_doesnt_have,
        
        })

def add_visit(request, sq_id):

    form = VisitForm(request.POST)

    if form.is_valid():
        new_visit = form.save(commit=False)
        #squirrel_id is the reference of Squirrel's _id,
        new_visit.squirrel_id = sq_id
        new_visit.save()

    return redirect('detail', sq_id = sq_id)


class SqCreate(CreateView):
    model = Squirrel
    fields = '__all__'

class SqDelete(DeleteView):
    model = Squirrel
    success_url = '/squirrels/'

class SqUpdate(UpdateView):
    model = Squirrel
    fields = ['species', 'description', 'country_found', 'age']


class FoodList(ListView):
    model = Food

class FoodDetail(DetailView):
    model = Food

class FoodUpdate(UpdateView):
    model = Food
    fields = ['name', 'foodtype']

class FoodDelete(DeleteView):
    model = Food
    success_url = '/food/'

def assoc_food(request, sq_id, food_id):
    Squirrel.objects.get(id=sq_id).food.add(food_id)
    return redirect('detail', sq_id = sq_id)