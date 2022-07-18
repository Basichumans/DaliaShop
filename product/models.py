
from unicodedata import category, name
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

        
    def __str__(self):
        return self.name
 
    
#additionaly create multiple  photos for the product
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #on delete cascade is used to delete the category if the product is deleted
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)                        #description
    price = models.IntegerField()                                                #price in cents
    created_at = models.DateTimeField(auto_now_add=True)                         #when created , automatically createated
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)       #upload_to - img saving folder
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)   #upload_to - img saving folder
    
    class Meta:
        ordering = ('-created_at',)                                             #to see creation date
    
    def __str__(self):
        return self.name
    
    
    
    def get_display_price(self):
        return self.price / 100                                                 # to see price in  $ converted from cents
    
    
    def get_thumbnail(self):                                                    #get the thumbnail or check if it exists
        if self.thumbnail:
            return self.thumbnail.url                                           # type: ignore
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)                # create thumbnail if it doesn't exist
                self.save()
                return self.thumbnail.url                                       # type: ignore
            else: 
                return'http://via.placeholder.com/240x240x.jpg'
                
                
    def make_thumbnail(self, image, size=(300,300)):                            #thumbnail maker
        img = Image.open(image)     
        img.convert('RGB')                                                      # convert to RGB if needed
        img.thumbnail(size)                                                     # resize image to 300x300
        
        thumb_io = BytesIO()    # 
        img.save(thumb_io, 'JPEG', quality=90)                                  # save the thumbnail
       
        thumbnail=File(thumb_io, name=image.name)                               # create a django file object/ thumbnail
        
        return thumbnail