from django.shortcuts import render
from django.views.generic import ListView
from blogs.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'homeaccount.html'

