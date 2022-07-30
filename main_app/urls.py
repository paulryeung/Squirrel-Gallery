from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('squirrels/', views.index, name='index'),
    path('squirrels/<int:sq_id>/', views.squirrel_details, name='detail'),
    path('squirrels/create/', views.SqCreate.as_view(), name='squirrels_create'),
    path('squirrels/<int:pk>/delete', views.SqDelete.as_view(), name='squirrels_delete'),
    path('squirrels/<int:pk>/update', views.SqUpdate.as_view(), name='squirrels_update'),
    path('squirrels/<int:sq_id>/add_visit/', views.add_visit, name='add_visit'),
    path('food/', views.FoodList.as_view(), name='food_index'),
    path('food/<int:pk>/', views.FoodDetail.as_view(), name='food_detail'),
    path('squirrel/<int:sq_id>/assoc_treat/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('squirrel/<int:sq_id>/unassoc_treat/<int:food_id>/', views.unassoc_food, name='unassoc_food'),
    path('accounts/signup/', views.signup, name='signup'),
]