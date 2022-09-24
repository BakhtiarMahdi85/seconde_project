from django import forms
from .models import Blog_Post

class Newpostform(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['text', 'title', 'status', 'author']
