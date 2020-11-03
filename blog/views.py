from django.shortcuts import render

# Create your views here.

# function that takes a request and returns a value received from 'render'
# 'render' will put together the template
def post_list(request):
    return render(request, 'blog/post_list.html', {})

