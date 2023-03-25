from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import GroceryItem


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def display_grocery(request):
    items = GroceryItem.objects.all()
    print("in function")
    return render(request, "BetterCart/grocerylist.html", {"items":items})

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

def finalizeListView(request):
    print("in finalize List View")