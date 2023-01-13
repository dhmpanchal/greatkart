from django.shortcuts import render
from django.views import View

# Create your views here.
class CartView(View):

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, 'thesite/cart.html', context)