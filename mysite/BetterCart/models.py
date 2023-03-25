from django.db import models

# Create your models here.
from django.db import models


class GroceryItem(models.Model):
    item_name = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name
