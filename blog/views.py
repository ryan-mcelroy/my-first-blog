from django.shortcuts import render
from django.utils import timezone #let us sort by time
from .models import Post       #lets us make things dynamic - connect model to template through view

# Create your views here.

# function that takes a request and returns a value received from 'render'
# 'render' will put together the template
def post_list(request):
    # new var that stores a QuerySet (published posts by date)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # pass 'posts' to render function
    # {} is a place to put stuff for the template to use
    # 'posts' must first be named: {'posts':posts}
    return render(request, 'blog/post_list.html', {})

