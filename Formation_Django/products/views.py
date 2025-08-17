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

"""def productCreate(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # Reset the form after saving
        message = "Product created successfully!"

    return render(request, 'products/create.html', {'form': form, 'message': message})"""


from django.shortcuts import render
from .models import Products

def productCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        slug = request.POST.get('slug')

        # Validation check
        if not name or not price:
            return render(request, 'products/create.html', {'message': "Name and Price are required!"})

        # Save product
        newProduct = Products.objects.create(
            name=name,
            description=description,
            price=price,
            image=image,
            slug=slug,
        )
        newProduct.save()

        return render(request, 'products/create.html', {'message': "Product created successfully!"})

    # GET request → just show the empty form
    return render(request, 'products/create.html')
