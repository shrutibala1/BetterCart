from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import GroceryItem


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def display_grocery(request):
    items = GroceryItem.objects.all()
    print("in function")
    return render(request, "BetterCart/grocerylist.html", {"items":items})