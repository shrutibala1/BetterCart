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

def add_grocery_item(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        new_item = GroceryItem(item_name=item_name)
        new_item.save()
        return redirect('grocery_list')
    else:
        return render(request, 'add_grocery_item.html')


# View function to remove a grocery item from the database
def remove_grocery_item(request, item_id):
    item_to_remove = GroceryItem.objects.get(id=item_id)
    item_to_remove.delete()
    return redirect('grocery_list')