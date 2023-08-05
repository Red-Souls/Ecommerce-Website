from django.shortcuts import render, redirect
from django.views import View
from .forms import*

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
        comments = Comment.objects.filter(post = id).order_by('-date')
        form = CommentForm()
        recentPosts = Post.objects.all().order_by('-date')[0:3]
        return render(request, 'pages/blog_detail.html', {
            'post': post,
            'comments': comments,
            'form': form,
            'recentPosts': recentPosts,
        })
    
    def post(self, request, id):
        form = CommentForm(request.POST)
        post = Post.objects.get(id = id)
        form.instance.post = post
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('/blog/')
        return redirect('/')

class SearchView(View):
    def get(self, request):
        return render(request, 'pages/blog_search.html')
    
    def post(self, request):
        search = request.POST['search']
        posts = Post.objects.filter(title__contains = search)
        return render(request, 'pages/blog_search.html', {
            'search': search,
            'posts': posts,
        })