from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category', default='cat.jpg')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
   


class Product(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product', default='cat.jpg')
    min_quant = models.IntegerField()
    max_quant = models.IntegerField()
    latest = models.BooleanField()
    best_seller = models.BooleanField()
    available = models.BooleanField()

    def __str__(self):
        return self.title 


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    paid_item = models.BooleanField(default=False)
    cart_no = models.CharField(max_length=36)

    def __str__(self):
        return self.user.username
    

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_item = models.BooleanField(default=False)
    cart_no = models.CharField(max_length=36)
    amount = models.IntegerField() 
    pay_code = models.CharField(max_length=36)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username