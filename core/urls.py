from django.urls import path
from core.views import frontpage, shop, signup,my_account, edit_my_account
from django.contrib.auth import views
from product.views import product



urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('myaccount/', my_account, name='myaccount'),
    path('edit_myaccount/', edit_my_account, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),                                          #<slug:slug> is the slug of the product to be loaded after clicking on the product / dinamic url
    path('singup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),                                  #views.LogoutView.as_view() is a function that returns to front page
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'), # 
]
    