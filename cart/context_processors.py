from .models import Cart, ItemInCart
from extras.utility import UtilityManager


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            the_utility = UtilityManager(request)
            the_cart = Cart.objects.filter(cart_id=the_utility.get_or_create_session())
            the_cart_items = ItemInCart.objects.filter(cart=the_cart[:1])
            for item in the_cart_items:
                cart_count += item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
    return dict(cart_count=cart_count)