import csv
from django.db import models
import sys

# Create your models here.
from django.db import models


class GroceryItem(models.Model):
    item_name = models.CharField(max_length=255)
    calories = models.IntegerField(null=True, blank=True)
    saturated_fat = models.FloatField(null=True, blank=True)
    unsaturated_fat = models.FloatField(null=True, blank=True)
    trans_fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.item_name

class nutriScore(models.Model):
    name = models.CharField(max_length=255)
    score = models.CharField(max_length=20)

    def __str__(self):
        return self.name



def load_data_from_csv():
    with open('string_nutriscore.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nutrition = nutriScore(
                name=row['\ufeffstr'],
                score=row['nutri_scores']
            )
            nutrition.save()
