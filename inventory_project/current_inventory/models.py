from django.db import models


class CurrentInventory(models.Model):
    inventoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    unitPrice = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.DecimalField(max_digits=11, decimal_places=2)
    minimalSupply = models.DecimalField(max_digits=11, decimal_places=2)

    def to_dict(self):
        data = {
            'inventoryID': self.inventoryID,
            'name': self.name,
            'unitPrice': self.unitPrice,
            'quantity': self.quantity,
            'inventoryValue': self.unitPrice * self.quantity,
            'minimalSupply': self.minimalSupply
        }
        return data


