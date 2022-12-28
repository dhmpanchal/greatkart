from django.shortcuts import render
from django.views import View

# Create your views here.
class SiteBaseView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'thesite/index.html')