# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'main/index.html',context)

def add_post(request):
    newpost = request.POST['post']
    Post.objects.create(post=newpost)
    posts = Post.objects.last()
    context = {
        'posts':posts
    }
    return render(request,'main/newPost.html',context)

