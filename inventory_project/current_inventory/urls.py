from django.urls import path

from . import views

urlpatterns = [
    path('currentInventory', views.current_inventory, name='currentInventory'),
    path('addInventoryItem', views.add_inventory_item, name='addInventoryItem'),
    path('updateInventoryItem', views.update_inventory_item, name='updateInventoryItem'),
    path('produceItem', views.produce_item, name='produceItem'),
]
