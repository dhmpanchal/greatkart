from django.shortcuts import render
from django.views import View
from store.models import Product

# Create your views here.
class SiteBaseView(View):

    def get(self, request, *args, **kwargs):
        context = {}

        products = Product.objects.filter(is_available=True)

        context = {
            'products': products,
        }
        return render(request, 'thesite/index.html', context)