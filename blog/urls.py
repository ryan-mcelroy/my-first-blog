from django.urls import path    # import the 'path' function from django
from . import views             # import all the views from 'blog' app (we don't have any yet)

urlpatterns = [                 # assigning a view called 'post_list' to root URL
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
]

