
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #on delete cascade is used to delete the category if the product is deleted
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)  #aprasymas
    price = models.IntegerField() # kad matyti centus
    created_at = models.DateTimeField(auto_now_add=True) # kada sukurtas, automatiskai sukuria irasa
    
    class Meta:
        ordering = ('-created_at',) #  kad matyti sukurimo data
    
    def __str__(self):
        return self.name
    
    
    
    def get_display_price(self):
        return self.price / 100 # kad matyti kainas in $
    