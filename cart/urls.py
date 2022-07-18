from django.urls import path
from cart.views import cart, add_to_cart,checkout,hx_menu_cart,update_cart,hx_cart_total



urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path ('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'), 
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),      #renders the cart decrement increment        
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),                               #renders the cart menu in the header                            
    path('hx_cart_total/', hx_menu_cart, name='hx_cart_total'),   
]                                                       