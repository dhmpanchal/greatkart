from django.shortcuts import render, get_object_or_404
from django.views import View
from store.models import Product
from category.models import Category

# Create your views here.
class StoreView(View):

    def get(self, request, category_slug=None, *args, **kwargs):
        context = {}
        categories = None
        products = None

        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category,is_available=True)
        else:
            products = Product.objects.filter(is_available=True)

        context = {
            'products': products,
            'total_products': products.count()
        }
        return render(request, 'thesite/store.html', context)

    
class ProductDetailView(View):
    
    def get(self, request, category_slug=None, product_slug=None, *args, **kwargs):
        context = {}
        
        try:
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        except Product.DoesNotExist as e:
            print(f"Product get failed==={e}")

        context = {
            'product': product,
        }

        return render(request, 'thesite/product_detail.html', context)