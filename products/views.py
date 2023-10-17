from django.shortcuts import render
from .models import Product



#home
def home(request):
    return render(request,'index.html')
#
def about(request):
    return render(request, 'about.html')

#Contact
def contact(request):
    return render(request, 'contact.html')


#fruit list
def list_fruits(request):
    fruits = Product.objects.filter(category='Fruits')
    return render(request, '#', {'fruits': fruits})

#fruit details
def fruit_detail(request, pk):
    fruit = Product.objects.get(id=pk,category='Fruits')
    return render(request, '#', {'fruit': fruit})

#vegetables list
def list_vegetables(request):
    fruits = Product.objects.filter(category='vegetables')
    return render(request, '#', {'fruits': fruits})

#vegtables list
def vegetable_detail(request, pk):
    fruit = Product.objects.get(id=pk,category='vegetables')
    return render(request, '#', {'fruit': fruit})

