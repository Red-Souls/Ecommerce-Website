from django.shortcuts import render
from django.views import View
from .forms import*

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'pages/register.html', {
            'form': form
        })
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/index.html')
        else:
            return render(request, 'pages/register.html', {
                'form': form
            })