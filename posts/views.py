from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django import forms

from posts.models import Post, Comment

# Create your views here.

class PostList(ListView):
	model = Post

class PostCreate(CreateView):
	model = Post
	fields = ['image', 'description', 'author']
	success_url = '/'

class CommentForm(forms.Form):
	comment = forms.CharField()