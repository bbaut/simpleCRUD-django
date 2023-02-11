from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def books(request):
    return render(request, 'books/index.html')

def create(request):
    return render(request, 'books/create.html')

def edit(request):
    return render(request, 'books/edit.html')