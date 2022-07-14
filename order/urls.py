from django.urls import path
from .views import create_order


urlpatterns = [
    path('create_order/', create_order, name='create_order'),      # import to main urls in DaliaShop app
]  
