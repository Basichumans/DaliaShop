"""DaliaShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Hom e
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
 
 

urlpatterns = [
    path('', include('core.urls')),                                  #core.urls is the file that contains the urls for the core app/ include is for redirecting to the core app urls
    path('cart/', include('cart.urls')),                             #cart.urls is the file that contains the urls for the cart
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #type: ignore
