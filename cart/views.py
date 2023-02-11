from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from store.models import Product
from .models import Cart, ItemInCart
from extras.utility import UtilityManager
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class CartView(View):

    def get(self, request, total=0, quantity=0, cart_items=None, *args, **kwargs):
        context = {}
        tax = 0
        grand_total = 0
        the_cart_items = None

        the_utility = UtilityManager(request)

        try:
            the_cart = Cart.objects.get(cart_id=the_utility.get_or_create_session())
            the_cart_items = ItemInCart.objects.filter(cart=the_cart, is_active=True)
            for cart_item in the_cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                quantity += cart_item.quantity
            tax = (2 * total)/100
            grand_total = total + tax
        except ObjectDoesNotExist:
            pass
        
        context = {
            'total': total,
            'quantity': quantity,
            'cart_items': the_cart_items,
            'tax': tax,
            'grand_total': grand_total,
        }
        return render(request, 'thesite/cart.html', context)

class AddCartView(View):

    def get(self, request, product_id, *args, **kwargs):
        the_product = Product.objects.get(id=product_id)

        the_utility = UtilityManager(request)

        try:
            the_cart = Cart.objects.get(cart_id=the_utility.get_or_create_session())
        except Cart.DoesNotExist:
            the_cart = Cart()
            the_cart.cart_id = the_utility.get_or_create_session()
            the_cart.save()

        the_cart.save() #if cart is already exists

        try:
            the_item_cart = ItemInCart.objects.get(product=the_product, cart=the_cart)
            the_item_cart.quantity += 1
            the_item_cart.save()
        except ItemInCart.DoesNotExist:
            the_item_cart = ItemInCart()
            the_item_cart.product = the_product
            the_item_cart.cart = the_cart
            the_item_cart.quantity = 1
            the_item_cart.is_active = True
            the_item_cart.save()

        return redirect('cart_view')

class RemoveCartView(View):

    def get(self, request, product_id, *args, **kwargs):
        the_utility = UtilityManager(request)
        the_cart = Cart.objects.get(cart_id=the_utility.get_or_create_session())
        product = get_object_or_404(Product, id=product_id)
        the_cart_item = ItemInCart.objects.get(product=product, cart=the_cart)
        if the_cart_item.quantity > 1:
            the_cart_item.quantity -= 1
            the_cart_item.save()
        else:
            the_cart_item.delete()
        return redirect('cart_view')

class RemoveCartItemView(View):

    def get(self, request, product_id, *args, **kwargs):
        the_utility = UtilityManager(request)
        the_cart = Cart.objects.get(cart_id=the_utility.get_or_create_session())
        product = get_object_or_404(Product, id=product_id)
        the_cart_item = ItemInCart.objects.get(product=product, cart=the_cart)
        the_cart_item.delete()
        return redirect('cart_view')