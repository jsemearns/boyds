from django.contrib import admin

from inventory.models import InventoryAction, Item, Supplier, Inventory
# Register your models here.

admin.site.register(InventoryAction)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Inventory)