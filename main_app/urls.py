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

]