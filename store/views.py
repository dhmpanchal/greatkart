from django.shortcuts import render, get_object_or_404
from django.views import View
from extras.utility import UtilityManager
from store.models import Product
from category.models import Category
from cart.models import ItemInCart
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
class StoreView(View):

    def get(self, request, category_slug=None, *args, **kwargs):
        context = {}
        categories = None
        products = None

        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category,is_available=True).order_by('id')
        else:
            products = Product.objects.filter(is_available=True).order_by('id')

        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)

        context = {
            'products': page_products,
            'total_products': products.count()
        }
        return render(request, 'thesite/store.html', context)

    
class ProductDetailView(View):
    
    def get(self, request, category_slug=None, product_slug=None, *args, **kwargs):
        context = {}
        
        try:
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
            the_utility = UtilityManager(request)
            in_cart = ItemInCart.objects.filter(cart__cart_id=the_utility.get_or_create_session()).exists()
        except Product.DoesNotExist as e:
            print(f"Product get failed==={e}")

        context = {
            'product': product,
            'in_cart': in_cart,
        }

        return render(request, 'thesite/product_detail.html', context)