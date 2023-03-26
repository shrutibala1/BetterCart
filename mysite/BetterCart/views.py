from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GroceryItem, nutriScore
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
            context=[]
            for row in reader:
                if search_string.lower() in row[1].lower() and row[1] not in results:
                    results.append(row[1])
                    try:
                        nutrition = nutriScore.objects.get(name=row[1])
                    except nutriScore.DoesNotExist:
                        nutrition = None
                    if nutrition:
                        context.append(nutrition.name + str(": ")+nutrition.score)
        return render(request, 'BetterCart/ingredient_search_results.html', {'results': results,'context':context})
    else:
        return render(request, 'BetterCart/add_grocery_item.html')


def recommendations(request, search_term):
    results = []
    with open('BetterCart/final_substitution.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        results.append(search_term.lower())
        try:
            nutrition = nutriScore.objects.get(name=search_term)
        except nutriScore.DoesNotExist:
            nutrition = None
        if nutrition:
            context2 = {
                'nutrition': nutrition.name,
                'score': nutrition.score
            }
        context = []
        for row in reader:
            if search_term.lower() in row[1].lower():
                results.append(row[3])
                try:
                    nutrition = nutriScore.objects.get(name=row[3])
                except nutriScore.DoesNotExist:
                    nutrition = None
                if nutrition:
                    context.append(nutrition.name + str(": ")+nutrition.score)

    return render(request, 'BetterCart/recommendations.html', {'results': results,'context2':context2,'context':context})


def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name', '')
        GroceryItem.objects.create(item_name=item_name)
        return redirect('/../../')
    else:
        return redirect('/../../')

def clear_list(request):
    GroceryItem.objects.all().delete()
    return redirect('/../../')