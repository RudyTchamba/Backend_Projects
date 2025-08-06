from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {"name": "Alice Smith", "age": 30},
        {"name": "Bob Johnson", "age": 25},
        {"name": "Charlie Brown", "age": 35},
        {"name": "Diana Prince", "age": 28},
        {"name": "Ethan Hunt", "age": 40},
        {"name": "Fiona Gallagher", "age": 22},
        {"name": "George Costanza", "age": 33},
        {"name": "Hannah Montana", "age": 20},
        {"name": "Ian Malcolm", "age": 45},
        {"name": "Julia Child", "age": 50},
    ]

    vegetables = ["Carrot", "Broccoli", "Spinach", "Potato", "Tomato"]

    return render(request, "home/index.html", context={"page": "Rudy retaking the basics in Django 2025", "peoples": peoples, "vegetables": vegetables})

def about(request):

    context = {"page" : "About"}

    return render(request, "home/about.html", context=context)

def contact(request):

    context = {"page" : "Contact"}

    return render(request, "home/contact.html", context=context)

def success_page(request):
    context = {"page" : "About"}
    return HttpResponse("<h1>This is a success page!</h1>")