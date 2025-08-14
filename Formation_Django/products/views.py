from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from .form import ProductForm

# Create your views here.
def product_list(request):
    products = Products.objects.all()  
    context = {
        'products': products
    }
    return render(request, 'products/details.html', context)

def productCreate(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # Reset the form after saving
        message = "Product created successfully!"

    return render(request, 'products/create.html', {'form': form, 'message': message})
