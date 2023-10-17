from django.urls import path
from . import views


urlpatterns = [
    #home
    path('home/', views.home, name='home'),
    #about 
    path('home/about/',views.about,name='about'),
    #contact
    path('home/contact/',views.contact,name='contact'),
    #list_fruit
    path('fruits/', views.list_fruits, name='list_fruits'),
    #fruit details
    path('fruits/<int:pk>/', views.fruit_detail, name='fruit_detail'),
    #vegtables list
    path('vegetables/', views.list_vegetables, name='list_vegetables'),
    #vegetable_detail
    path('vegetables/<int:pk>/', views.vegetable_detail, name='vegetable_detail'),
]