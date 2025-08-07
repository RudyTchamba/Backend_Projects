from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "index.html")

def contact(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Us</h1>")

def blog(request, *args, **kwargs):
    return HttpResponse("<h1>Blog Page</h1>")
