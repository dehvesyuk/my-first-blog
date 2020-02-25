<<<<<<< HEAD
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
=======
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
>>>>>>> 4965e6431a33a8d43ab50b239391aa37aab20c92
    return render(request, 'blog/post_list.html', {'posts': posts})