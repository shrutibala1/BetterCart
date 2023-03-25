from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grocerylist/', views.display_grocery, name = 'display grocery'),
    path('add-item/', views.addItemView, name='add-item'),
    path('finalize-list/', views.finalizeListView, name='finalize-list'),
]