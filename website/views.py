from django.shortcuts import render
from .models import Product, Sanatorium

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    all_products = Product.objects.all()
    all_sanatoriums = Sanatorium.objects.all()
    return render(request, 'products.html', {'products': all_products, 'sanatoriums': all_sanatoriums})

def contact(request):
    return render(request, 'contact.html')

def sanatoriums(request):
    all_products = Sanatorium.objects.all()
    return render(request, 'products.html', {'sanatoriums': all_products})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
