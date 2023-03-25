from django.shortcuts import render
from .models import GroceryItem

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# View function to add a new grocery item to the database
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
