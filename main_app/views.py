from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Squirrel, Food
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import VisitForm

#for user login and signup forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#user signup
def signup(request):
    error_message=''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            #login via code
            login(request, user)
            return redirect('index')
        else:
            #error_message= 'Invalid sign up - try again'
            error_message = form.errors

    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



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
    #update this field, no longer '__all__' but specify fields ['name', 'age' ...]
    fields = ['name', 'species', 'description', 'country_found', 'age']

    def form_valid(self, form):
        #assign logged in user to squirrel
        form.instance.user = self.request.user  #form.instance is the squirrel
        
        return super().form_valid(form)

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