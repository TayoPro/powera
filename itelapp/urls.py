from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.catgories, name='categories'),
    path('products/', views.products, name='products'),
    path('category/<str:id>/', views.category, name='category'),
    path('product/<str:id>/', views.product, name='product'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logoutpage, name='logoutpage'),
    path('register/', views.registerpage, name='registerpage'),
    path('password/', views.password, name='password'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('deleteitem/', views.deleteitem, name='deleteitem'),
    path('increase/', views.increase, name='increase'),
    path('checkout/', views.checkout, name='checkout' ),
    path('sendorder/', views.sendorder, name='sendorder'),
    path('completed/', views.completed, name='completed')
]


