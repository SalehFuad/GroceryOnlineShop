from django.urls import path
from . import views


urlpatterns = [
    #home
    path('home/', views.home, name='home'),
    #about 
    path('home/about/',views.about,name='about'),
    #contact
    path('home/contact/',views.contact,name='contact'),
   #products_list
    path('home/products/', views.product_list, name='products'),
 
 #product details
    path('home/products/<int:pk>/',views.product_detail, name='product'),]