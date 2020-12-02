from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404


def home(request):
    posts = Post.objects.all().order_by('-published_on')
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'details.html', {'post': post})


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
