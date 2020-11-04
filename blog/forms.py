from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta: 
        model = Post # which model to be used to create the form
        fields = ('title', 'text',) #which fields whould be in our form
        