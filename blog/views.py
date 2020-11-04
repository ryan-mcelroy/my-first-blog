from django.shortcuts import render
from django.shortcuts import get_object_or_404  # allow for non-existant objects
from django.utils import timezone               # let us sort by time
from .models import Post        # lets us make things dynamic - connect model to template through view
from .forms import PostForm     # import the new PostForm model

# Create your views here.

# function that takes a request and returns a value received from 'render'
# 'render' will put together the template
def post_list(request):
    # new var that stores a QuerySet (published posts by date)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # pass 'posts' to render function
    # {} is a place to put stuff for the template to use
    # 'posts' must first be named: {'posts':posts}
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #handles cases where no post of pk exists
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})