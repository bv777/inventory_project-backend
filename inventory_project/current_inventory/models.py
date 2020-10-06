from django.db import models


class CurrentInventory(models.Model):
    inventoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.DecimalField(max_digits=11, decimal_places=2)
    minimal_supply = models.DecimalField(max_digits=11, decimal_places=2)

    def to_dict(self):
        data = {
            'inventoryID': self.inventoryID,
            'name': self.name,
            'unitPrice': self.unit_price,
            'quantity': self.quantity,
            'inventoryValue': self.unit_price * self.quantity,
            'minimalSupply': self.minimal_supply
        }
        return data


class ProductionLog(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    inventory_item = models.ForeignKey(CurrentInventory, on_delete=models.DO_NOTHING)
    productionID = models.AutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=11, decimal_places=2)

    def to_dict(self):
        data = {
            'dateTime': self.date_time,
            'inventoryID': self.inventory_item,
            'productionID': self.productionID,
            'quantity': self.quantity
        }
        return data
