from . models import ShopCart



def counter(request):
    basket = ShopCart.objects.filter(user__username= request.user.username, paid_item=False)

    cart_read = 0
    for item in basket:
        cart_read += item.quantity

    context = {
        'cart_read':cart_read
    }

    return context