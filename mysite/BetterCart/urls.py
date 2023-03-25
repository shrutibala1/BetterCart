from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_grocery, name='index'),
    # path('grocerylist/', views.display_grocery, name = 'display grocery'),
    path('add-item/', views.addItemView, name='add-item'),
    path('finalize-list/', views.finalizeListView, name='finalize-list'),
    path('add_grocery_filled_item/', views.addItemFilledView, name='add-item-filled'),
    path('ingredient_search_result/', views.addItemFilledView, name='add-item-filled'),
    path('ingredient_search/', views.ingredient_search, name='ingredient_search'),

]