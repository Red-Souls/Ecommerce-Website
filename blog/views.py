from django.shortcuts import render, redirect
from django.views import View
from .models import*

# Create your views here.
class HomeView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        return render(request, 'pages/blog.html', {
            'posts': posts,
        })

class BlogDetail(View):
    def get(self, request, id):
        post = Post.objects.get(id = id)
        return render(request, 'pages/blog_detail.html', {
            'post': post,
        })