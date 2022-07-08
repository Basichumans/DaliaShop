
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,redirect
from product.models import Product, Category
from .forms import SignUpForm


# Create your views here.

#my account method   (login required if for onli loged users to see this page)
@login_required
def my_account(request):
    return render(request, 'core/myaccount.html')

# my account method for information edditing
@login_required
def edit_my_account(request):
    if request.method == 'POST' :                                             #gets the data from , post tag in the form
        user = request.user                                                   #using iterables to update the data in the database
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        
        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')
   

#front page
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


#shop method
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