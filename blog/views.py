from django.shortcuts import redirect # allows us to direct to new url
from django.shortcuts import render
from django.shortcuts import get_object_or_404  # allow for non-existant objects
from django.utils import timezone               # let us sort by time
from .models import Post        # lets us make things dynamic - connect model to template through view
from .forms import PostForm     # import the new PostForm model


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
    if request.method == "POST": # if there's data to submit, construct PostForm with the data
        form = PostForm(request.POST)
        if form.is_valid():      # check form data has been entered correctly so we can save it
            post = form.save(commit=False) # soft-save, allows us to add other details below
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # save the blog post
            return redirect('post_detail', pk=post.pk) # direct to the post_detail view if new blogpost created
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST": 
        form = PostForm(request.POST, instance=post)
        if form.is_valid():      
            post = form.save(commit=False) 
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) 
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})