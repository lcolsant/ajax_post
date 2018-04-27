# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'main/index.html')

def add_post(request):
    print 'got here'
    context = {
        'post':request.POST['post']
    }
    return render(request, 'main/index.html',context)

# Create your views here.
