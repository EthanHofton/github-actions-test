from django.db import models


# Create your models here.
class ShoppingListItem(models.Model):
    itemName = models.CharField(max_length=256)
    itemPrice = models.IntegerField()

    def __str__(self):
        return self.itemName
