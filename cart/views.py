from django.shortcuts import render
from .cart import Cart



# Create your views here.

#must be added to urls.py file  from DaliaShop/
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/menu_cart.html')