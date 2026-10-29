from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    products = [
        {'product': 'Laptop', 'price': 2500},
        {'product': 'Mouse', 'price': 80},
        {'product': 'Keyboard', 'price': 150},
        {'product': 'Monitor', 'price': 700},
    ]
    return render(request, 'products.html', {'product': products })