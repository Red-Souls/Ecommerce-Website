from django.shortcuts import render, redirect
from django.views import View
from .forms import*

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'pages/index.html', {
            'products': products,
        })
    
    def post(self, request):
        products = Product.objects.all()
        form = OrderForm()
        return render(request, 'pages/index.html', {
            'products': products,
            'form': form,
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
    
class CartView(View):
    def get(self, request):
        try:
            Cart.objects.get(user = request.user)
        except:
            cart = Cart()
            cart.user = request.user
            cart.save()

        cart = Cart.objects.get(user = request.user)
        cartItem = cart.cartItem.all()
        return render(request, 'pages/cart.html', {
            'cart': cartItem,
        })
    
    def delete(self, request):
        pass
    
class OrderView(View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        form = OrderForm()
        return render(request, 'pages/order.html', {
            'product': product,
            'form': form,
        })
    
    def post(self, request, id):
        product = Product.objects.get(id = id)
        cart = Cart.objects.get(user = request.user)
        print(cart)
        form = OrderForm(request.POST)
        form.instance.product = product
        form.instance.price = product.price
        if form.is_valid():
            item = form.save()
            cart.cartItem.add(item)
            cart.save()
            return redirect('/cart/')
        return render(request, 'pages/order.html', {
            'product': product,
            'form': form,
        })