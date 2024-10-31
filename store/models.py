from django.db import models
from users.models import User


# Categoies 
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
# Product
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # one to many relation
    Description = models.TextField(max_length=250, default='', blank=True, null=True)
    Image = models.ImageField(upload_to='uploads/product/')    
    # image will vbe uploaded in 'media/uploads/product' - cf MEDIAFILE
         
    def __str__(self) -> str:
        return self.name

# Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False) 
    
    def __str__(self) -> str:
        return self.product