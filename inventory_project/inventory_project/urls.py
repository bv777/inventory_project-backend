from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/inventoryManagment/', include('current_inventory.urls')),
    path('admin/', admin.site.urls),
]
