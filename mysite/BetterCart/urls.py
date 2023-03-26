from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_grocery, name='index'),
    # path('grocerylist/', views.display_grocery, name = 'display grocery'),
    path('BetterCart/add-item/', views.addItemView, name='add-item'),
    path('BetterCart/finalize-list/', views.finalizeListView, name='finalize-list'),
    path('BetterCart/add_grocery_filled_item/', views.addItemFilledView, name='add-item-filled'),
    path('BetterCart/ingredient_search_result/', views.addItemFilledView, name='add-item-filled'),
    path('BetterCart/ingredient_search/', views.ingredient_search, name='ingredient_search'),

]