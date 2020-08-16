from django.urls import path

from . import views

urlpatterns = [
    path('currentInventory', views.current_inventory, name='currentInventory'),
    path('addInventoryItem', views.add_inventory_item, name='addInventoryItem'),
]
