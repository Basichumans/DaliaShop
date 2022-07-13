from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.models import Product
from .cart import Cart



# Create your views here.

def tprice(quantity, product):
    tottalprice= (quantity * product.price)/100
    return tottalprice
    pass


#must be added to urls.py file  from DaliaShop/
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/menu_cart.html')


def cart(request):  
    return render(request, 'cart/cart.html')


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')


def hx_menu_cart(request):                                       #renders the cart menu in the header
    return render(request, 'cart/menu_cart.html')


def hx_cart_total(request):                                       
    return render(request, 'cart/partials/cart_total.html')

    
def update_cart(request,product_id, action):                        #method for cart increment decrement| action is either add or remove| product_id for update
    cart = Cart(request)
    if action == 'increment':
        cart.add(product_id, 1, True)                               #True means update the quantity
    else:
        cart.add(product_id,-1 , True)                              #-1 means remove the product
    
    #for htmx get the product from data base    
    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']                #get the quantity because get_item returns a dictionary
    
    #dictionary for item to return to the cart
    item = { 'product':{    
                            'id':product.id,
                            'name':product.name,
                            'image':product.image,
                            'get_thumbnail':product.get_thumbnail(),
                            'price':product.price,
    },
            'total_price':(quantity * product.price)/100,
            'quantity':quantity,
            }
    #return the item object 
    response  = render(request, 'cart/cart_item.html', {'item':item}) 
    response ['HX-Trigger'] = 'update-menu-cart'                #this trigger is for htmx to update the cart
    return response

