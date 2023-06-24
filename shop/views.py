from django.shortcuts import render
from django.views import View
from .models import*

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'pages/index.html', {
            'products': products,
        })
    
class ProductDetail(View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        return render(request, 'pages/product_detail.html', {
            'product': product,
        })
    
class SearchView(View):
    def get(self, request):
        return render(request, 'pages/search.html')
    
    def post(self, request):
        search = request.POST['search']
        products = Product.objects.filter(name__contains = search)
        return render(request, 'pages/search.html', {
            'search': search,
            'products': products,
        })