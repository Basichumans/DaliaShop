
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render,redirect
from product.models import Product, Category
from .forms import SignUpForm


# Create your views here.
def frontpage(request): 
    products = Product.objects.all()[0:8]                                    #how many products to show on the frontpage
    
    return render(request, 'core/frontPage.html', {'products': products})    #pass the products to the frontpage

#signup method
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})



#login method
def login_(request):
    return render(request, 'core/login.html') 


def  shop(request):
    categories = Category.objects.all() #get all categories
    products = Product.objects.all() #get all products
    
    active_category = request.GET.get('category', '') #get the category from the url
    
    if active_category:
        products = products.filter(category__slug=active_category) #filters the products by category
    
    query = request.GET.get('query', '') #get the query from the url
    if query:
        products = products.filter(Q(name__icontains = query) | Q(description__icontains=query)) #icontains = insensitive  capital case, Q describtion is for similar search
        
    
    context = {'categories': categories,
               'products': products,
               'active_category': active_category
               } 
    
    return render(request, 'core/shop.html', context) #render the shop page