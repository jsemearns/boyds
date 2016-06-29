from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=128)
	stock_on_hand = models.IntegerField()

	def __unicode__(self):
		return self.name


class Supplier(models.Model):
	name = models.CharField(max_length=128)
	contact = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name


class Inventory(models.Model):
	item = models.ForeignKey(Item)
	supplier = models.ForeignKey(Supplier)

	def __unicode__(self):
		return '{} - {}'.format(self.item, self.supplier)


class InventoryAction(models.Model):
	date = models.DateField()
	quantity = models.IntegerField()
	cost = models.FloatField(blank=True)
	is_in = models.BooleanField(default=True)
	inventory = models.ForeignKey(Inventory)