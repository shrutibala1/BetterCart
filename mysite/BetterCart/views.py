from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Add a new grocery item to the database
def add_grocery_item(item_name, index):
    new_item = GroceryItem(item_name=item_name, index=index)
    new_item.save()

# Remove a grocery item from the database
def remove_grocery_item(item_id):
    item_to_remove = GroceryItem.objects.get(id=item_id)
    item_to_remove.delete()