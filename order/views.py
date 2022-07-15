from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart

# Create your views here.
# Check if order is goin though, after click
def create_order(request):
    cart = Cart(request)
    
    if request.method =='POST':
        #get the data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        #create order
        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, address=address, phone=phone)

        #loop through the cart items
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        return redirect('myaccount')               #redirect to myaccount page  from core template
    return redirect('cart')                        # if not post request, redirect to cart 

