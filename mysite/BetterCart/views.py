from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GroceryItem
import requests
from bs4 import BeautifulSoup
from .scraper import scrape_foodsubs
import csv




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def display_grocery(request):
    items = GroceryItem.objects.all()
    print("in function")
    return render(request, "BetterCart/grocerylist.html", {"items": items})


def addItemView(request):
    print("in add item views")
    return render(request, 'BetterCart/add_grocery_item.html')
    # if request.method == 'POST':
    #     item_name = request.POST['item_name']
    #     new_item = GroceryItem(item_name=item_name)
    #     new_item.save()
    #     return redirect('grocery_list')
    # else:
    #     return render(request, 'add_grocery_item.html')


def addItemFilledView(request):
    print("in add item (filled) views")
    return render(request, 'BetterCart/add_grocery_filled_item.html')


def finalizeListView(request):
    print("in finalize List View")


def ingredient_search(request):
    return render(request, 'BetterCart/ingredient_search.html')


def ingredient_search(request):
    if request.method == 'POST':
        search_string = request.POST.get('search_term', '')
        results = []
        with open('BetterCart/final_substitution.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                if search_string.lower() in row[1].lower():
                    results.append(row[3])
        return render(request, 'BetterCart/ingredient_search_results.html', {'results': results})
    else:
        return render(request, 'BetterCart/add_grocery_item.html')
