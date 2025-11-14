from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')

# Create your views here.
