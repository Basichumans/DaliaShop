from django.shortcuts import render, get_object_or_404
from . models import Product    

# Create your views here.
def product(request, slug):     
    product = get_object_or_404(Product, slug=slug)    #get the product from the database
    return render(request, 'product/product.html', {'product': product}) #pass the product to the product page