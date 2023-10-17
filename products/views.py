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
def product_list(request):
   # products= Product.objects.all()
    return render(request,'product-list.html')

#fruit details
def product_detail(request, pk):
   # product = Product.objects.get(id=pk)
    return render(request, 'product-detail.html')

#vegetables list
