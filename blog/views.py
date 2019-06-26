from django.shortcuts import render,redirect
from .practical.practice import subtract
from .practical.e1 import toolbar_all

from django.contrib import messages
import requests
from .forms import  ProfileUpdateForm

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def execute(request):
    return render(request, 'blog/execute.html')

def output(request):
    #data=requests.get("https://www.google.com/")
    #print(data.text)
    a=5
    b=6
    c=a+b
    sub=subtract(a,b)
    data=c,sub
    #data=data.text
    return render(request, 'blog/execute.html', {'data': data})

def profile(request):
    toolbar_all()
    return render(request, 'blog/profile.html')


