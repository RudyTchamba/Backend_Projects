from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def product_list(request):
    products = Products.objects.get(id=1)  
    context = {
        'products': products
    }
    return render(request, 'products/details.html', context)
