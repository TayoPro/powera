from django.contrib import admin
from . models import Category, Product, ShopCart,Payment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','image')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','category_id','category','title','image','price','min_quant','max_quant','latest','best_seller','available')


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','quantity','paid_item','cart_no')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','user','paid_item','cart_no','amount','pay_code','first_name','last_name','phone','address','state')



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Payment,PaymentAdmin)
