from django.conf import settings

from product.models import Product


class Cart(object):     
    def __init__(self, request):                                        #access the cart from the session
        self.session= request.session                                   #get the session
        cart = self.session.get(settings.CART_SESSION_ID)               #get the cart from the session from the settings.py
        
        if not cart:                                                    #if the cart is created or not
            cart = self.session[settings.CART_SESSION_ID] = {}          #create a new cart if it doesn't exist
        
        
        self.cart = cart                                                #to use this object in the modules
        
    def __iter__(self):
        for p in self.cart.keys():                                    #iterate through the cart , keys are id of the products
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)   #isignet to the item, get the product from the database, str is used to convert the id to string, pk to get the id from the database
            
        for item in self.cart.values():                                      #iterate through the cart, values are the items in the cart
            item['total_price']= int(item['quantity'] * item['product'].price) /100  #get the total price of the product
            yield item                                                      #yield the item
    
    def __len__(self):                                                  #get the length of the cart, how many items are in the cart
        return sum(item['quantity'] for item in self.cart.values())     #return the number of items in the cart
    
    def save(self):                                                     #save the cart to the session,notify the server that smthg has changed
        self.session[settings.CART_SESSION_ID] = self.cart              #save the cart in the session
        self.session.modified = True                                    # sesion have been updated
        
    def add(self, product_id, quantity=1, update_quantity=False):        #add a product to the cart, update the quantity to update the cart
        product_id = str(product_id)                                     #convert the id to string to easear get it from self.cart
        
        if product_id not in self.cart:                                  #if the product is not in the cart
            self.cart[product_id] = {'quantity': 1, 'id': product_id}   
            
            
        if  update_quantity:                                             # increment od decrement the quantity in the cart
            self.cart[product_id]['quantity'] += int(quantity)           #add the quantity to the cart
            
            if self.cart[product_id]['quantity'] == 0 :                  #if the quantity is 0 remoce the product from the cart
                self.remove(product_id)                                  #remove the product from the cart
            
        self.save()
        
        
    def remove(self, product_id):                                        #remove a product from the cart
        if product_id in self.cart:                                      #if the product is in the self.art
            del self.cart[product_id]                                    #delete the product from the cart
            self.save()                                                  #save the cart
            
            
    def get_tottal_cost(self):                                           #get the total cost of the cart
        for p in self.cart.keys():                                      #iterate through the cart, keys are id of the products
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        return int(sum(item['total_price'] for item in self.cart.values()))/100  #return the total cost of the cart