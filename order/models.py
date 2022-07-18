from django.db import models
from django.contrib.auth.models import User 
from product.models import Product 

# Create your models here.
# Model for buyer
'''
for order we need  user shipping address,
billing address, order status, 
'''
class Order(models.Model):
    user = models.ForeignKey(User,related_name= 'orders', on_delete=models.CASCADE, blank=True, null=True)  #blank=True, null=True for guest users
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
   
    
    created = models.DateTimeField(auto_now_add=True) #
    
    paid = models.BooleanField(default=False)                                   # if the order is paid or not
    paid_amount = models.IntegerField(blank=True,null=True)                     # null turue because the amount paid  dont know yet
    
    #create stattus field for the order in database
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    
    #for admin interface
    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),       
    )
    #status to 
    status = models.CharField(max_length=256, choices=STATUS_CHOICES,  default='ORDERED')

    
   

# Model for order item 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    
    def get_display_price(self):
        return self.price / 100 
   
    def get_tottal_cost(self):                                                    
        for item in self.order.items.all():
            return item.price