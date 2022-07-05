from .cart import Cart


#must be added to settings.py file  templates context_processors
#method to see the cart  everythere in the application
def cart(request):           
    cart = Cart(request)    
    return {'cart': cart}   #pass the cart to the template



# def cart(request):
#     return {'cart': Cart(request)}