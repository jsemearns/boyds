from django import forms

from inventory.models import Item, Supplier, Inventory


class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ['name', 'stock_on_hand']


class SupplierForm(forms.ModelForm):

	class Meta:
		model = Supplier
		fields = ['name', 'contact']


class InventoryForm(forms.ModelForm):

	class Meta:
		model = Inventory
		fields = ['item', 'supplier']